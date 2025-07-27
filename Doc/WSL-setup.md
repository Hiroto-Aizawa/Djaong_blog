# 【WSL のセットアップ方法】

## 事前準備

・Windows10（バージョン 2004 以降）または、Windows11
・管理者権限を持つアカウント（設定 > アカウントで確認できる）
・PC がインターネットに接続している

## 開発環境

・Windows10/11
・PowerShell（Win マークで右クリ > PowerShewll 管理者権限で実行）

## 導入方法

### WSL の有効か

1. 管理者権限で PowerShell を開く

1. 以下のコマンドを実行して WSL を有効化する  
   `wsl --install`

1. インストールが完了したら、ユーザー名とパスワードの設定を求められる。  
   そんなのでできてないんだが、、、

1. 利用可能なディストリビューションを確認する  
   `wsl --list --online`

   **※このアプリケーションには、Linux 用 Windows サブシステムオプションコンポーネントが必要です。次を実行してインストールする： wsl.exe --install --nodistribution**  
   と表示された場合は、上記のコマンドを実行してください

1. 好みのディストリビューションを選択してインストールする  
   Ubuntu をインストールする場合は、以下のようにコマンドを実行する  
   `wsl --install Ubuntu`

### WSL2 を既定のバージョンに設定

1. WSL2 を既定のバージョンに設定する  
   `wsl --set-default-version 2`

### インストールの確認

1. インストールされたディストリビューションを確認する  
   `wsl -l -v` = `wsl --list --verbose`

1. 出力に選択したディストリビューション（例：Ubuntu）が表示され、バージョンが 2 になっていることを確認する

### WSL の起動と使用

1. Powershell で以下のコマンドを実行して、WSL を起動する
   `wsl`

1. これにより、デフォルトの Linux ディストリビューション（通常は Ubuntu）が起動します。

1. 特定のディストリビューションを起動したい場合は、以下のコマンドを使用します。  
   `wsl -d <ディストリビューション名>`  
   例えば、Ubuntu を起動する場合：  
   `wsl -d Ubuntu`

## 参考サイト

・[WSL のインストール](https://learn.microsoft.com/ja-jp/windows/wsl/install)

・[Windows(WSL2)上に Django 開発環境を構築する](https://qiita.com/tsubonnyu/items/cbcd6a377eb4dc18d09a)

・[[Windows] 新しく PC 買ったので WSL2 を導入してみる](https://zenn.dev/ap_com/articles/install-wsl2-on-windows)

・[WSL2 + Ubuntu + VSCode での開発環境構築](https://qiita.com/zaburo/items/27b5b819fae2bde97a3bQda3)
