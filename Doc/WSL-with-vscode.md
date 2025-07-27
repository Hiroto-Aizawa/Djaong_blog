# VSCode で WSL 環境を構築する

## Ubuntu でのセットアップ

1. VSCode の termial から以下コマンドを実行して、Ubuntu をアップデートする  
   `sudo apt update && apt upgrade`

1. pip のインストール

```bash:bash
sudo apt install python3-pip
```

1. venv のインストール  
   python3.~の数字は自身の環境にインストールされているバージョンを入力する  
   バージョンは`python3 --version`を実行することで確認できる

```
sudo apt install python3.12-venv
```

1. プロジェクトフォルダの作成

```
mkdir SampleProject
cd SampleProject
```

1. 仮想環境の作成

```
python3 -m venv sample
source sample/bin/activate
```

activate 実行後に、先頭が`(sample)`となっていれば仮想環境に接続できている

```
(sample) user@user:~$/SampleProject
```

## Visual Studio Code の設定

1. Remote - Development 拡張機能をインストールする
1. これまで作業していたプロジェクトフォルダ上でコマンドを実行して、WSL2 上の VSCode リモートサーバーを起動する

```
code .
```

1. VSCode が起動し、左下に`WSL:Ubuntu~`と表示されればリモートサーバーに接続できている

1. WSL2 側に Python の拡張機能をインストールする必要がある。

## Django のインストール

1. 仮想環境を有効にする

```
source sample/bin/activate
```

1. Django のインストール

```
python3 -m pip intall django
```

## 参考サイト

・[Windows(WSL2)上に Django 開発環境を構築する](https://qiita.com/tsubonnyu/items/cbcd6a377eb4dc18d09a)
