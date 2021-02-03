# blog
![ブログ](https://yuhi-sa.github.io/)の管理用フォルダ
- Hugo + github Pagesで作成
- [Beautiful Hugo](https://themes.gohugo.io/beautifulhugo/)!

## hugo 実行方法
ローカルのサーバーで確認
```
hugo server
```
ローカルのサーバーで確認(ドラフトも対象)
```
hugo server -D
```
公開用ファイルを作成
```
hugo
```
publicフォルダをgithub.ioのフォルダにpush


## latex 数式を使うための編集
/layouts/partials/add_mathjax.htmlを作成
```
<script>
    MathJax = {
        tex: {
        inlineMath: [['$', '$'], ['\\(', '\\)']]
        }
    };
</script>

<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
```

/layouts/partials/site-header.htmlに追記
```
{{ partial "add_mathjax.html" . }}
```
参考：[MathJaxを用いてHugoで数式を表現する](https://somei-tec.com/article/computer-science/framework/hugo/hugo_mathjax/)