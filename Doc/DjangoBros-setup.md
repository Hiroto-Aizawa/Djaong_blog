# Python3 と Django の環境を構築する

## WSL をインストールしていない場合

1. Win マークを右クリックし、管理者権限で Powershell を起動する

1. WSL のインストール

   Powershell で下記コマンドを入力し、実行する

   ```
   wsl --install
   ```

1. Ubuntu のアップデート

   Ubuntu コンソールで以下を実行して、Ubuntu をアップデートする

   ```
   sudo apt update && apt upgrade
   ```

1. インストール・アップデートが完了したら PC を再起動する

1. 再起動すると、ユーザー名を設定する画面が表示される  
   画面が表示されなければ、検索バーから「Ubuntu」を検索して起動する

1. ユーザー名、パスワードを設定すれば WSL が使えるようになります

1. WSL のバージョン確認

   ```
   wsl -l -v
   ```

## Python のインストール

1. Win マークを右クリックして、PowerShell を管理者権限で起動する

1. sudo apt install python3-pip

## 仮想環境（venv）のインストール

Django 以外の環境と共存させるために、venv の仮想環境上に Django 環境を構築する

1. venv のインストール

   ここでは、python3.12 に対応する venv をインストールする

   ```
   sudo apt install python3.12-venv
   ```

1. pip のインストール

   pip は Python のパッケージ管理システムです。  
   ライブラリやパッケージを簡単にインストールしたり、バージョン管理したりできるシステムのことです。  
   この後 Django をインストールするので先に pip をインストールしておきます

   ```
   sudo apt install python3-pip
   ```

1. プロジェクトフォルダの作成

   ```
   mkdir DjangoBros
   cd DjangoBros
   ```

1. 仮想環境作成

   djangobros_venv という名前の仮想環境を作成後、有効化する

   ```
   python3 -m venv djangobros_venv
   source djangobros_vnev/bin/activate
   ```

   有効化後にシェルの先頭に仮想環境名が表示されていれば、仮想環境に接続できている

   ```
   (djangobros_venv) user@user:$~/DjangoBros
   ```

   仮想環境から抜ける場合は、以下のコマンドを実行する

   ```
   deactivate
   ```

   ※Django は仮想環境内にインストールしているため、deactivate 後は使用できないことに注意してください

1. Django のインストール

   仮想環境にいる状態で、Django をインストールします。

   ```
   (djangobros_venv) ~/DjangoBros$ python3 -m pip install django

   または

   (djangobros_venv) ~/DjangoBros$ sudo apt install python3-django
   ```

## 参考サイト

・[WSL のインストール](https://learn.microsoft.com/ja-jp/windows/wsl/install)

・[Windows(WSL2)上に Django 開発環境を構築する](https://qiita.com/tsubonnyu/items/cbcd6a377eb4dc18d09a)

・[[Windows] 新しく PC 買ったので WSL2 を導入してみる](https://zenn.dev/ap_com/articles/install-wsl2-on-windows)

・[WSL2 + Ubuntu + VSCode での開発環境構築](https://qiita.com/zaburo/items/27b5b819fae2bde97a3bQda3)
