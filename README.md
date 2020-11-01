##  概要

Google Vision APIテストアクセス

##  実行環境

* VScode
* dcoker-compose + Remote-Containers

##  事前準備

* Dokcer Desktopインストール
* VScodeインストール
* VScodeのExstensitonでRemote - Containersをインストール
* ディレクトリ作成、GCPサービスアカウントキー配置
    - TODO 環境変数設定に変える
```zsh
mkdir ~/docker_home/vision_api
mkdir ~/vision_api/google_key
# google_key配下にGCPサービスアカウントキー配置
```

###  プロジェクトの起動

* Command + Shift + P または画面左下緑の矢印からメニューを開き「Open Folder in Container」を選択
* このリポジトリフォルダを開く

### 参考

* https://qiita.com/d0ne1s/items/d2649801c6f804019db7
* https://blog.serverworks.co.jp/tech/2020/07/15/codevelop-with-docker/