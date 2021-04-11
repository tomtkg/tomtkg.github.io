---
layout: default
title: Tom TKG's Homepage
---

[受賞歴](#受賞歴)  
[PCにインストールしているもの](#pcにインストールしているもの)  
[進化計算学会の簡易まとめ](#進化計算学会の簡易まとめ)  
[Matlabで図を作成する関数](#matlabで図を作成する関数)  
[Springer LNCSスタイルファイルのダウンロード方法](#springer-lncsスタイルファイルのダウンロード方法)  
[IEEEなどの投稿規定を満たすPDF作成方法](#ieeeなどの投稿規定を満たすpdf作成方法)  
[参考文献スタイルファイル (.bst)変更メモ](#参考文献スタイルファイル-bst変更メモ)  

### 受賞歴
- 電気学会 2019年 電子・情報・システム部門大会 奨励賞
- IEEE CIS 日本支部 YRA (進化計算シンポジウム2020)
- 進化計算コンペティション2020 単目的部門トップ賞
- 進化計算コンペティション2020 多目的部門トップ賞
- 令和2年度 電気通信大学 学生表彰

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

### 進化計算学会の簡易まとめ
進化計算学会論文誌に掲載されている論文を表形式でまとめた．  
[表: 進化計算学会論文誌の論文](data/tjpnsec){:target="_blank"}  
著者は4人まで載せている．著者が5人以上の論文も一部あるため，参考文献を書くときは注意されたい．

論文タイトルを用いてWord Cloudを作成した．  
<a href="image/tjpnsec.png"><img src="image/tjpnsec.png"/></a>  
頻出単語は'最適化'，'進化'，'提案'，'問題'，'目的'，'計算'，'探索'，'評価'，'設計'であった．

進化計算学会が主催している会議の論文を表形式でまとめた．  
[表: 進化計算学会主催会議の論文](data/jpnsec){:target="_blank"}  
著者は4人まで載せている．著者が5人以上の論文も一部あるため，参考文献を書くときは注意されたい．  
ページ数の情報が一部欠落している．また，論文の中身は非公開となっている．

論文タイトルを用いてWord Cloudを作成した．  
<a href="image/jpnsec.png"><img src="image/jpnsec.png"/></a>  
会議の論文では'提案'と同じくらい'検討'が多くなっている．  
遺伝的アルゴリズム GA，MOEA/D，差分進化 DE，粒子群最適化 PSOなど有名なアルゴリズムのワードが増えている．  
'対話型'，並列'，'考慮'，'利用'，'解析'など実世界で使うことに関するワードが増えている．

### Matlabで図を作成する関数
自分がMatlabで3次元の図を作成するときに使っている関数．  
区間[0-1]に正規化された3次元の点群dataとその名前nameを入力する．

{% highlight matlab linenos %}
function SaveImage(data,name)
    figure('Position',[100 100 500 500],'Visible','on');
    set(gca,'Fontname','Times New Roman','FontSize',13,'NextPlot','add', ...
        'Color','none','Box','on','View',[135 30],'LooseInset', get(gca, 'TightInset'));
    plot3(data(:,1),data(:,2),data(:,3),'o','MarkerSize',8, ...
        'Markerfacecolor',[.7 .7 .7],'Markeredgecolor',[.4 .4 .4]);
    xlim([-0.05 1.05]); xlabel('\it f\rm_1','position',[0.4,1.2,-0.15]);
    ylim([-0.05 1.05]); ylabel('\it f\rm_2','position',[1.2,0.4,-0.15]);
    zlim([-0.05 1.05]); zlabel('\it f\rm_3','position',[0.4,-0.77,0.5],'Rotation',0);
    zticks([0 0.5 1]); axis square;
    exportgraphics(gcf,[name,'.pdf'],'BackgroundColor','none','ContentType','vector');
    exportgraphics(gcf,[name,'.emf'],'BackgroundColor','none','ContentType','vector');
    savefig([name,'.fig']); close;
end
{% endhighlight %}

図は正方形で余白は極めて小さい．11行目にブレ-クポイントを設定して，目視で確認することが多い．  
画像はベクタ形式の透過背景で保存．論文にはpdf，パワーポイントにはemfで出力した画像を用いる．  
左は自分の設定で生成されるベクタ画像．右はmatlabの基本設定で生成されるラスタ画像．

<p><embed src="image/image.pdf#toolbar=0&navpanes=0&scrollbar=0&view=FitB" type="application/pdf" width="300" height="315"><a href="image/image.jpg"><img src="image/image.jpg" width="420"/></a></p>

### Springer LNCSスタイルファイルのダウンロード方法
まず最初に，2021年3月10日時点でのSpringer LNCSスタイルファイルのURLを示す.  
ftp://ftp.springernature.com/cs-proceeding/llncs/llncs2e.zip  
Springer LNCSのURLは，http，httpsではなくftpから始まっている．  
Google Chrome，Microsoft Edgeなどはftpへの対応を止めたため，通常の設定ではファイルのダウンロードが不可能となっている．  
ファイルをダウンロードする一番簡単な解決策はInternet Explorerで上記URLを開くことである．  
ただし，安全に利用できないとして他のウェブブラウザでは利用を非推奨・不可能にしているものを，開発が終了した古いウェブブラウザを使って安全でない状態で利用する点に注意されたい．  
他の手段，スタンドアロンのFTPソフトウエアを利用する方法でもダウンロードができる．  
Springerがftpを利用しないファイル提供方法を用意することを期待したい．(ファイルの再頒布許可を期待したい）

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

<a href="image/memo1.png"><img src="image/memo1.png" width="336"/></a>
<a href="image/memo2.jpg"><img src="image/memo2.jpg" width="410"/></a>

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
