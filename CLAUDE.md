# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Hugo blog (https://yuhi-sa.github.io/) with the `tomatohugo` theme. Japanese default with English translations. Deployed to GitHub Pages via GitHub Actions on push to `main`.

## Commands

```bash
# Dev server
hugo server

# Dev server with drafts
hugo server -D

# Production build (what CI runs)
hugo --gc --minify

# Format check (what CI and pre-commit hook run)
npm run format:check

# Auto-fix formatting
npm run format
```

## Architecture

### Repository Structure

- `config.toml` — Hugo site configuration (languages, menus, params, taxonomies)
- `content/posts/` — Blog posts in Markdown (Japanese `1.md` + English `1.en.md`)
- `themes/tomatohugo/` — Theme as a **git submodule** (`git@github.com:yuhi-sa/tomatohugo.git`); has its own CLAUDE.md with detailed theme architecture
- `public/` — Build output; deployed to `yuhi-sa/yuhi-sa.github.io` repo by CI (not committed here)
- `.github/workflows/deploy.yml` — CI/CD pipeline (Hugo 0.155.3 extended)

### Theme (tomatohugo)

The theme is an independent repository. When modifying theme files, work inside `themes/tomatohugo/` and commit there separately. See `themes/tomatohugo/CLAUDE.md` for theme-specific architecture (template inheritance, partials, asset pipeline, dark mode, SEO).

Key theme paths:

- `layouts/` — Templates (posts/, pages/, taxonomy/, partials/)
- `assets/css/` — Plain CSS with custom properties (variables.css, main.css, syntax.css)
- `assets/js/` — dark-mode.js

### Content Front Matter

Posts support: `title`, `date`, `description`, `tags`, `categories`, `images`, `math` (enables MathJax), `noindex`, `draft`

### Deployment Flow

Push to `main` → GitHub Actions: checkout with submodules → `npm ci` → Prettier check → Hugo build → deploy to `yuhi-sa/yuhi-sa.github.io`

## Conventions

- **Commit messages**: conventional commits — `type(scope): description`
- **Formatting**: Prettier enforced via Lefthook pre-commit hook (CSS/JS/MD checked; HTML templates excluded)
- **CSS**: BEM naming, CSS custom properties for theming, no SCSS
- **Indentation**: 2 spaces

## GA4 Data-Driven Content Workflow

GA4（MCP analytics-mcp）からデータを取得し、ブログの改善・新規記事追加を行う手順。

### Step 1: GA4データ取得

```
# アカウント・プロパティ確認
get_account_summaries → property_id を特定

# 過去90日の人気記事（PV順）
run_report:
  property_id, date_ranges: [90daysAgo ~ yesterday]
  dimensions: [pagePath, pageTitle]
  metrics: [screenPageViews, averageSessionDuration, bounceRate]
  order_bys: screenPageViews desc, limit: 30

# 流入元分析
run_report:
  dimensions: [sessionSource, sessionMedium]
  metrics: [sessions, screenPageViews]

# 検索クエリ分析（Search Console連携がある場合）
run_report:
  dimensions: [searchTerm]
  metrics: [screenPageViews]

# タグ別パフォーマンス（pagePath から手動集計）
```

### Step 2: データ分析・記事企画

取得データから以下を判断:

- **人気カテゴリの特定**: PV上位記事のタグを集計し、伸びている分野を把握
- **関連記事の不足**: 人気記事と同タグで関連する未執筆テーマを洗い出す
- **SEO機会**: 検索流入があるが記事が薄いトピック
- **滞在時間/離脱率**: 改善が必要な既存記事の特定

企画時の判断基準:

| 指標                         | 目安                                   |
| ---------------------------- | -------------------------------------- |
| 高PV + 高離脱率              | 既存記事の改善（内容追加・内部リンク） |
| 高PV カテゴリ + 関連記事不足 | 新規記事追加（シリーズ化）             |
| 検索流入あり + 記事なし      | 新規記事作成（SEO狙い）                |

### Step 3: 記事執筆（チームエージェント並行）

```
TeamCreate → TaskCreate（記事ごと）→ Task（writer エージェント並行起動）
```

- 1記事 = 1エージェント、JA + EN の2ファイルを同時作成
- 既存記事を Read して文体・深度を合わせる
- DA（Devil's Advocate）が技術的正確性・数式・コード品質をレビュー
- Reviewer が全体整合性・フォーマット・ビルドを検証

### Step 4: 記事フォーマット仕様

```yaml
# JA版 front matter
---
title: "日本語タイトル"
date: YYYY-MM-DDTHH:MM:SS+09:00
draft: false
description: "説明文"
tags: ["日本語タグ", "Python"] # Python/Matplotlib等はそのまま
keywords: ["日本語タグ", "Python"]
math: true # 数式を含む場合のみ
---
<!--more-->
# EN版 front matter
---
title: "English Title"
date: YYYY-MM-DDTHH:MM:SS+09:00 # JA と同じ日時
draft: false
description: "Description"
tags: ["English Tag", "Python"]
---
<!--more-->
```

- ディレクトリ: `content/posts/YYYYMMDD_TopicName/`
- ファイル: `1.md`（JA）+ `1.en.md`（EN）
- 数式: `$...$`（inline）、`$$...$$`（display）、`\tag{N}` で番号付け
- コード: ` ```python `
- 内部リンク: `{{< ref "/posts/YYYYMMDD_Topic/1.md" >}}`（JA）、`1.en.md`（EN）
- JA タグは日本語（機械学習, フィルタリング等）、EN タグは英語

### Step 5: 検証・デプロイ

```bash
hugo --gc --minify        # ビルドエラーなし確認
npm run format:check      # Prettier通過確認（失敗時 npm run format）
hugo server               # ローカルで表示確認
git add → git commit → git push  # CI/CD で自動デプロイ
```

### Step 6: 効果測定（次回セッション）

デプロイ2〜4週間後に再度 GA4 データを取得し、新規記事のパフォーマンスを確認:

```
run_report:
  dimension_filter: pagePath contains "20260223"  # 日付でフィルタ
  metrics: [screenPageViews, averageSessionDuration, bounceRate]
```

目標対比で評価し、次の改善サイクルに回す。
