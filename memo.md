---
layout: default
title: Tom TKG's Homepage
---

### PCにインストールしているもの
- ウェブブラウザ：Edge, Chrome.
- エディタ：sakura-editor, VS Code.
- コミュニケーション：Slack, Zoom.
- ファイル共有：Dropbox, Google drive.
- プログラミング：Matlab, Python.
- 論文作成：Grammarly, Ghostscript, GSview.
- EPS：Metafile to EPS Converter.
- Git：Git Bash, GitHub Desktop.
- PDF：pdf_as, Sumatra PDF.
- Tex：TexStudio, TeXWorks.
- Unix：Docker, GnuWin32, WSL.
- その他：7-Zip, OpenVPN, MPC-HC, MS Office, WinMerge.

### IEEEなどの投稿規定を満たすPDF作成方法
IEEEなどに投稿する最終論文は，学会が用意した機械的なチェックをクリアしないと投稿できない．  
採択の通知から最終投稿までの期間が短く，論文チェック可能な回数も制限があるので注意が必要.  
ローカルで論文チェックする方法と修正方法：
- texのコンパイルはplatexではなく，pdflatexを使う
- pdffontsコマンドで使われているフォント情報を確認
    - pdffonts hoge.pdfで全体確認
    - pdffonts -f 5 -l 6 hoge.pdf で5,6ページ目だけ確認
- Syntax ErrorかType3が表示されたらアウト
- 基本的にeps画像が悪いと考えてよい
- パワーポイントの画像をepsにするならMetafile to EPS Converterを使う．かつ詳細オプションのTrueTypeフォントとダウンロードオプションを画像のように変更
- texlive使っているならgs_pdfwr.ps 33行目 standardfonts内の項目をコメントアウトする

<a href="image/memo1.png"><img src="image/memo1.png" width="300"/></a>
<a href="image/memo2.jpg"><img src="image/memo2.jpg" width="365"/></a>

### 参考文献スタイルファイル (.bst)変更メモ
文献リストファイル (.bib)の中身はGoogle ScholarのBibTexを参考にする  
jpnsec.bstで変更した部分
- Line 84,85: ": " -> ", "
- Line 245: "{ll,\~~}{vv~}{f.}{, jj}" -> "{f.~~}{ll}{vv~}{, jj}"
- Line 302: 'title -> {title  "``" swap$ * "''" * }
- Line 336: {" (" year * ")" * } -> {", " year * "." * }
- Line 525,530,573,580,630,677,682,687: "in" -> ""
- Line 837,846: organization output -> 
- Line 1036: -> MACRO {tec}  {"IEEE Trans. on Evolutionary Computation"}

後はbib, bblを自由に変更する (journal, booktitleなど)

左：変更前，右：変更後

<a href="image/memo3.png"><img src="image/memo3.png"/></a>