# blog
[ブログ](https://yuhi-sa.github.io/)の管理用フォルダ
- Hugo + github Pagesで作成
- [Beautiful Hugo](https://themes.gohugo.io/beautifulhugo/)

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

# google Analytics
config.tomlに追加
```
googleAnalytics = "測定ID"

```
Google Analyticsとの連携のための組み込みテンプレート({{ template "_internal/google_analytics_async.html" . }})が古いため変更を追加  

layouts/partials/head.html
```
- {{ template "_internal/google_analytics_async.html" . }}
+ {{- partial "analytics" . -}}
```
layouts/partials/analytics.htmlを作成
```
{{ if not .Site.IsServer }}
{{ with .Site.GoogleAnalytics }}
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id={{ . }}"></script>
<script>
   window.dataLayer = window.dataLayer || [];
   function gtag(){dataLayer.push(arguments);}
   gtag('js', new Date());
   gtag('config', '{{ . }}');
</script>
{{ end }}
{{ end }}
```
参考：[Hugoで未だ対応していないgtag.jsを利用して Googleアナリティクスする](https://qiita.com/momotaro98/items/4de7934fd79cd6b34fce)