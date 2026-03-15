#!/usr/bin/env python3
"""記事テーマ自動提案スクリプト

既存記事のタグ・カテゴリを分析し、人気タグについて
Gemini APIを使って未執筆テーマを提案する。

Usage:
    python scripts/suggest_topics.py
    python scripts/suggest_topics.py --top 10
    python scripts/suggest_topics.py --slack
"""

import argparse
import json
import os
import re
import sys
import urllib.request
from collections import Counter
from pathlib import Path

CONTENT_DIR = Path(__file__).resolve().parent.parent / "content" / "posts"
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"


def parse_front_matter(filepath: Path) -> dict:
    """Hugoの YAML front matter から tags と categories を抽出する。"""
    try:
        text = filepath.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return {}

    # front matter は --- で囲まれた部分
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return {}

    fm_text = match.group(1)
    result = {}

    for key in ("tags", "categories"):
        # tags: ["tag1", "tag2"] 形式を解析
        pattern = rf'^{key}:\s*\[(.*?)\]'
        m = re.search(pattern, fm_text, re.MULTILINE)
        if m:
            raw = m.group(1)
            # "tag1", "tag2" からタグを抽出
            items = re.findall(r'"([^"]*)"', raw)
            if items:
                result[key] = items

    # title も取得（提案時の参考情報として）
    title_match = re.search(r'^title:\s*"(.+?)"', fm_text, re.MULTILINE)
    if title_match:
        result["title"] = title_match.group(1)

    return result


def collect_articles(content_dir: Path) -> list[dict]:
    """content/posts/ 以下の日本語記事 (1.md) からメタ情報を収集する。"""
    articles = []
    if not content_dir.exists():
        print(f"Error: {content_dir} が見つかりません", file=sys.stderr)
        sys.exit(1)

    for post_dir in sorted(content_dir.iterdir()):
        if not post_dir.is_dir():
            continue
        md_file = post_dir / "1.md"
        if not md_file.exists():
            continue

        meta = parse_front_matter(md_file)
        if meta:
            meta["dir_name"] = post_dir.name
            articles.append(meta)

    return articles


def analyze_tags(articles: list[dict], top_n: int = 10) -> list[tuple[str, int]]:
    """タグの出現頻度を集計し、上位 top_n を返す。"""
    tag_counter: Counter[str] = Counter()
    for article in articles:
        for tag in article.get("tags", []):
            tag_counter[tag] += 1
    return tag_counter.most_common(top_n)


def get_articles_by_tag(articles: list[dict], tag: str) -> list[str]:
    """指定タグを持つ記事のタイトルリストを返す。"""
    titles = []
    for article in articles:
        if tag in article.get("tags", []):
            title = article.get("title", article.get("dir_name", "不明"))
            titles.append(title)
    return titles


def suggest_with_gemini(
    tag: str,
    existing_titles: list[str],
    all_tags: list[tuple[str, int]],
    api_key: str,
) -> str:
    """Gemini API で未執筆テーマを提案させる。"""
    existing_list = "\n".join(f"- {t}" for t in existing_titles)
    tag_summary = ", ".join(f"{t}({c}件)" for t, c in all_tags)

    prompt = f"""あなたは技術ブログのコンテンツプランナーです。

以下は技術ブログの「{tag}」タグに関する情報です。

## ブログ全体のタグ分布
{tag_summary}

## 「{tag}」タグの既存記事（{len(existing_titles)}件）
{existing_list}

## タスク
「{tag}」タグで、まだカバーされていないサブトピックを5つ提案してください。

条件:
- 既存記事と重複しないテーマを選ぶ
- 技術ブログとして実用的で、読者のニーズが高いテーマ
- 各提案には「タイトル案」と「概要（1-2文）」を含める
- 関連する既存記事があれば、シリーズ化や内部リンクの観点も考慮
- 日本語で回答

## 出力フォーマット
1. **タイトル案**: 概要
2. **タイトル案**: 概要
...
"""

    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0.8,
            "maxOutputTokens": 1024,
        },
    }

    url = f"{GEMINI_API_URL}?key={api_key}"
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            candidates = result.get("candidates", [])
            if candidates:
                parts = candidates[0].get("content", {}).get("parts", [])
                if parts:
                    return parts[0].get("text", "（応答なし）")
            return "（Gemini APIから有効な応答が得られませんでした）"
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        return f"（Gemini APIエラー: {e.code} {body[:200]}）"
    except Exception as e:
        return f"（Gemini API呼び出しエラー: {e}）"


def build_markdown_report(
    top_tags: list[tuple[str, int]],
    suggestions: dict[str, str],
    total_articles: int,
) -> str:
    """結果をMarkdown形式でフォーマットする。"""
    lines = []
    lines.append("# 記事テーマ自動提案レポート")
    lines.append("")
    lines.append(f"**総記事数**: {total_articles}")
    lines.append(f"**分析対象タグ数**: {len(top_tags)}")
    lines.append("")

    lines.append("## 人気タグランキング")
    lines.append("")
    lines.append("| 順位 | タグ | 記事数 |")
    lines.append("|------|------|--------|")
    for i, (tag, count) in enumerate(top_tags, 1):
        lines.append(f"| {i} | {tag} | {count} |")
    lines.append("")

    lines.append("---")
    lines.append("")

    for tag, suggestion in suggestions.items():
        count = next((c for t, c in top_tags if t == tag), 0)
        lines.append(f"## {tag}（既存 {count} 件）の未執筆テーマ提案")
        lines.append("")
        lines.append(suggestion)
        lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def build_slack_payload(report: str) -> dict:
    """Slack Webhook用のペイロードを生成する。"""
    # Markdownをそのままtextとして送信（Slackはmrkdwn形式で解釈）
    return {"text": report}


def send_to_slack(payload: dict, webhook_url: str) -> bool:
    """Slack Webhookにメッセージを送信する。"""
    req = urllib.request.Request(
        webhook_url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.status == 200
    except Exception as e:
        print(f"Slack送信エラー: {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(
        description="既存記事のタグを分析し、未執筆テーマを提案する"
    )
    parser.add_argument(
        "--top",
        type=int,
        default=5,
        help="分析対象の人気タグ数（デフォルト: 5）",
    )
    parser.add_argument(
        "--slack",
        action="store_true",
        help="結果をSlack Webhookで送信する",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Gemini APIを呼ばずにタグ分析のみ実行する",
    )
    args = parser.parse_args()

    # 記事収集
    articles = collect_articles(CONTENT_DIR)
    print(f"記事を {len(articles)} 件収集しました。", file=sys.stderr)

    # タグ分析
    top_tags = analyze_tags(articles, top_n=args.top)
    if not top_tags:
        print("タグが見つかりませんでした。", file=sys.stderr)
        sys.exit(1)

    print(f"人気タグ上位 {len(top_tags)} 件:", file=sys.stderr)
    for tag, count in top_tags:
        print(f"  {tag}: {count} 件", file=sys.stderr)

    if args.dry_run:
        # dry-run: タグ分析結果のみ表示
        report = build_markdown_report(top_tags, {}, len(articles))
        print(report)
        return

    # Gemini API キー確認
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print(
            "Error: 環境変数 GEMINI_API_KEY が設定されていません。",
            file=sys.stderr,
        )
        print("--dry-run オプションでタグ分析のみ実行できます。", file=sys.stderr)
        sys.exit(1)

    # 各人気タグについて提案を取得
    suggestions: dict[str, str] = {}
    for tag, count in top_tags:
        print(f"「{tag}」の提案を取得中...", file=sys.stderr)
        existing = get_articles_by_tag(articles, tag)
        suggestion = suggest_with_gemini(tag, existing, top_tags, api_key)
        suggestions[tag] = suggestion

    # レポート生成
    report = build_markdown_report(top_tags, suggestions, len(articles))
    print(report)

    # Slack送信
    if args.slack:
        webhook_url = os.environ.get("SLACK_WEBHOOK_URL")
        if not webhook_url:
            print(
                "Error: 環境変数 SLACK_WEBHOOK_URL が設定されていません。",
                file=sys.stderr,
            )
            sys.exit(1)

        payload = build_slack_payload(report)
        if send_to_slack(payload, webhook_url):
            print("Slackに送信しました。", file=sys.stderr)
        else:
            print("Slack送信に失敗しました。", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
