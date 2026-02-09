#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

MSG="${1:-Publishing changes}"

# キャッシュクリアとビルド
rm -rf resources/_gen
hugo --gc --minify

# publicディレクトリ（GitHub Pages サブモジュール）をコミット＆プッシュ
cd public
git add .
if git diff --cached --quiet; then
  echo "public: 変更なし、スキップ"
else
  git commit -m "$MSG"
  git push
  echo "public: プッシュ完了"
fi

# ルートディレクトリをコミット＆プッシュ
cd ..
git add .
if git diff --cached --quiet; then
  echo "root: 変更なし、スキップ"
else
  git commit -m "$MSG"
  git push
  echo "root: プッシュ完了"
fi

echo "デプロイ完了"
