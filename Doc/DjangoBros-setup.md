# Python3 と Django の環境を構築する

## WSL をインストールしていない場合

1. Win マークを右クリックし、管理者権限で Powershell を起動する

1. WSL のインストール
   Powershell で下記コマンドを入力し、実行する

   ```
   wsl --install
   ```

1. Ubuntu のアップデート

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
