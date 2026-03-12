#!/bin/bash
# Daily blog post creation + GA4 stats notification
# Runs via launchd every morning at 9:00

set -euo pipefail

export PATH="/Users/yuhi-sa/.local/bin:/usr/local/bin:/opt/homebrew/bin:$PATH"
export HOME="/Users/yuhi-sa"
unset CLAUDECODE

WORKDIR="/Users/yuhi-sa/Hobby/blog.com"
LOGFILE="${WORKDIR}/logs/daily_blog_$(date +%Y%m%d).log"

cd "$WORKDIR"

echo "=== Daily Blog Job Started: $(date) ===" >> "$LOGFILE"

claude -p \
  --permission-mode bypassPermissions \
  --model sonnet \
  --max-budget-usd 5 \
  "以下の手順を順番に実行してください。

## Step 1: GA4データ取得
analytics-mcp の run_report で過去7日間のデータを取得:
- property_id: \"261042911\"
- date_ranges: [{\"start_date\": \"7daysAgo\", \"end_date\": \"yesterday\"}]
- dimensions: [{\"name\": \"pagePath\"}, {\"name\": \"pageTitle\"}]
- metrics: [{\"name\": \"screenPageViews\"}, {\"name\": \"averageSessionDuration\"}, {\"name\": \"bounceRate\"}]
- order_bys: [{\"metric\": {\"metric_name\": \"screenPageViews\"}, \"desc\": true}]
- limit: 20

全体セッション数も取得:
- dimensions: [{\"name\": \"sessionSource\"}, {\"name\": \"sessionMedium\"}]
- metrics: [{\"name\": \"sessions\"}, {\"name\": \"screenPageViews\"}]

## Step 2: データ分析＆記事企画
取得データから:
- PV上位記事のタグ・カテゴリを確認（既存記事をReadして確認）
- 人気カテゴリで関連記事が不足しているテーマを1つ選定

## Step 3: 記事作成
CLAUDE.mdの「記事フォーマット仕様」に従い、JA + EN の2ファイルを作成:
- ディレクトリ: content/posts/YYYYMMDD_TopicName/ (今日の日付を使用)
- ファイル: 1.md (JA) + 1.en.md (EN)
- 既存記事を数本読んで文体・深度を合わせる
- front matterのフォーマットを厳守
- 技術的に正確で実用的な内容にする

## Step 4: ビルド検証
hugo --gc --minify を実行。
npm run format:check を実行。失敗したら npm run format してリトライ。

## Step 5: Slack通知
以下のフォーマットでSlackに通知を送信:

curl -X POST -H 'Content-type: application/json' \
  --data '{\"text\": \"📊 *GA4 Weekly Report (過去7日間)*\n\n*PV上位5記事:*\n1. [記事名] - [PV数] PV\n2. ...\n\n*全体統計:*\n- 総セッション数: [数]\n- 総PV数: [数]\n\n*流入元TOP3:*\n1. [source/medium] - [sessions]\n...\n\n📝 *新規記事作成:*\n- [作成した記事タイトル]\n- パス: [ファイルパス]\n- 選定理由: [理由]\n\n⚠️ ビルド結果: [成功/失敗]\"}' \
  \$SLACK_WEBHOOK_URL

実際のデータで組み立ててください。

## Step 6: Git commit & push
記事ファイルのみをgit addして conventional commit でコミット:
feat(content): add new article on [トピック名]

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

コミット後、git push origin main を実行してデプロイしてください。" \
  >> "$LOGFILE" 2>&1

echo "=== Daily Blog Job Finished: $(date) ===" >> "$LOGFILE"
