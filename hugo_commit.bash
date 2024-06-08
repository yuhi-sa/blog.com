# Hugoのビルド
hugo --minify

# publicディレクトリに移動して変更をコミット
cd public
git add .
git commit -m "Publishing changes"
git push

# ルートディレクトリに戻って変更をコミット
cd ..
git add .
git commit -m "Publishing changes"
git push
