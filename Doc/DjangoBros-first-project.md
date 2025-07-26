# 初めてのプロジェクトを作ろう

## プロジェクトとアプリケーション

1. DjangoBros ディレクトリに移動して仮想環境を有効にする

   ```
   source djangobros_venv/bin/activate
   (djangobros_venv) user@user:$~/DjangoBros
   ```

1. プロジェクトの作成

   「django_blog」というプロジェクトを作成する
   作成後にそのディレクトリに移動し、構成を確認する

   ```
   (djangobros_venv) $ django-admin startproject django_blog
   (djangobros_venv) $ cd django_blog
   (djangobros_venv) $ ls
   ```

## 基本的なディレクトリ構成

1. ディレクトリは以下のような構成になっています

   ```
   ~DjangoBros/django_blog
   django_blog
   manage.py
   ```

   manage.py は Django プロジェクトを管理・運用する際に使うファイルです。  
   サーバーを立ち上げる際、プロジェクトの管理者情報を作成する時に使用する。  
   基本的にこのファイルの中身を編集することはない。

1. Python パッケージ

   django_blog はこのプロジェクトの Python パッケージです。中には４つのファイルが含まれています。

   1. init.py: django_blog が Python パッケージであることを示すための空ファイルです。こちらを変更することはありません
   1. settings.py: Django プロジェクトの設定ファイルです。今後様々な場面で利用します。
   1. urls.py: ウェブサイトの各ページの URL を設定するファイルです。
   1. wsgi.py: サーバーの設定などを行うファイルです。

## 初めての Django ページを表示しよう

1. プロジェクトのルートディレクトリに移動する。

   ルートディレクトリ：1 番上の階層

   今回の場合は、「DjangoBros/django_blog」がルートディレクトリになっています。

   ls コマンドで直下に「manage.py」があることを確認し、ローカルサーバーを起動させる

   ※python3 manage.py ~ というコマンドは manage.py の 1 階層上にいる状態でないと使用できない点に注意が必要です。

   ```
   (djangobros_venv) $ ls
   django_blog manage.py
   (djangobros_venv) $ python3 manage.py runserver
   ```

   サーバー起動後に「http://127.0.0.1:8000/」にアクセスするとDjangoのデフォルトページが表示されます。

   サーバーを停止するときは、ターミナルで`Ctrl + C`を押す

## settings.py で設定してみよう

1. settings.py の言語設定を編集する

   ```
   LANGUAGE_CODE = 'ja'
   ```

1. TIME_ZONE の設定

   ```
   TIME_ZONE = 'Asia.Tokyo'
   ```

1. データベースを作ろう

   Django ではデフォルトで「sqlite3」というデータベースを使用するように settings.py で以下のように設定されている

   ```
   DATABASES = {
      'default' : {
         'ENGINE' : 'django.db.backends.sqlite3',
         'NAME' : BASE_DIR / 'db.sqlite3',
      }
   }
   ```

   この状態では、データベースの指定だけでまだ作成されていません。

   ルートディレクトリで`python3 manage.py migrate`を実行してデータベースを作成します。

   ```
   (djangobros_venv) $ python3 manage.py migrate
   Operations to perform:
      Apply all migrations: admin, auth, contenttypes, sessions
   Running migrations:
      Applying auth.0001_initial... OK
      .......
   ```

   上記のような出力を確認できればデータベースが作成されています。

   `python3 manage.py migrate`はデータベースの設計に変更がされた際に、データベースに変更を反映するコマンドです。
