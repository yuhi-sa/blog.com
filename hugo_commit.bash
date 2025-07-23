# Hugoのキャッシュクリアとビルド
rm -rf resources/_gen
hugo --cleanDestinationDir

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
