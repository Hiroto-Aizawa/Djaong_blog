# アプリケーションで機能を作ろう

## アプリケーションの作成

プロジェクトのルートディレクトリでアプリケーション作成コマンドを実行する

1. アプリケーションの作成

   ```
   (djangobros_venv) ~/DjangoBros/django_blog/$ python3 manage.py startapp blogs
   ```

   ルート直下に`blogs`フォルダが作成されていれば完了  
   blogs 内にあるファイルにコードを書いて、様々な機能を実装していきます

## アプリケーションの登録

1. プロジェクトにアプリケーションを登録する

   `python3 manage.py startapp`でアプリケーションを作成した後に、Django プロジェクトに登録する必要があります。

   django_blog/settings.py を開いて、`INSTALL_APPS`の部分に作成した`blogs`を追加します。

   ```
   INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ####blogsを追加###
    'blogs'
   ]
   ```

   これで Django プロジェクト内でアプリケーションとして扱われるようになります。
   登録をしていないと、アプリケーションを編集してもプロジェクトに反映されないので、忘れずに登録しましょう

## Templates でページを作ろう

アプリケーションの登録ができたので、シンプルな Web ページを作成します

1. テンプレートの作成

   Django で扱う HTML ファイルは動的なコードを扱えるため、Python のコードを書くことができます  
   Django ではそのような HTML ファイルを`Templates`と呼びます。

   テンプレートを作成するために`blogs`ディレクトリに移動して以下のコマンドを実行する  
   ※VSCode で作業している場合はマウス操作でフォルダを作成しても良い

   ```
    (djangobros_venv) ~//django_blog/blogs$ mkdir templates
    (djangobros_venv) ~//django_blog/blogs$ cd templates
    (djangobros_venv) ~//django_blog/blogs/templates$ mkdir blogs
   ```

   上記コマンドによって`django_blog/blogs/templates/blogs`ディレクトリが作成されました。  
    Django では、このようにアプリケーション内に作成した`templates/<アプリケーション名>`ディレクトリ内にテンプレートを配置します。

   アプリケーション内に同名のフォルダを作成しているため冗長のように見えますが、このような構成になっている理由は別のチュートリアルで説明します。

1. html ファイルの作成

   `templates/blogs/`内に`index.html`を作成します

   ```
   (djangobros_venv) ~//django_blog/blogs/templates/blogs$ touch index.html
   ```

   `index.html`を作成後、html ファイルを以下のように編集します。

   ```
   <html>
       <h1>ブログサイト</h1>
       <p>ここはトップページです</p>
   </html>
   ```

   HTML ファイルは作成できましたが、どの URL の時にこのファイルを表示していいかを Django が把握できていません。  
   そのため、次はこのテンプレートファイルと URL を結びつけます

## View とは

トップページを表示させるために、`View`を作成します。  
Django における View とは、ユーザーから送られてきたリクエストをもとに、どの HTML ファイルを表示させるか、どういった内容のデータを表示させるかなどを決める処理をしています。

1. views.py の中身を見る

   `blogs/views.py`を開き、以下のようにコードを書いてください。

   ```
   ###~djanbo_blog/blogs/views.py###

   from django.shortcuts import render

   def index(request):
      return render(request, 'blogs/index.html')
   ```

   index 関数では、引数に`request`を取っています。  
   ここでの request とは、ユーザーが URL を入力してサーバーにアクセスする際に送られる情報のことを指します。

   この関数は、ユーザーからの`request情報`をもとに、`render`を`return`しています。  
   `render`メソッドは、request 情報をもとに index.html を表示しています。

   このことから、index 関数は「ユーザーからの情報をもとに、index.html を返す」関数です。

# URL の設定

作成した index 関数を特定の URL と紐づけて、ユーザーがその URL を打ち込んだ時に index.html ファイルがブラウザ上で表示されるようにします。

1. urls.py の設定

   `django_blogs/django_bros/urls.py`を開き、以下のように修正します。  
    ※プロジェクト全体の URL 設定

   ```
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
      path('admin/', admin.site.urls),
      path('', include('blogs.urls')),
   ]
   ```

   2 行目の import で`include`を追記していることで、include 関数が使用可能になります。

   `path('', include('blogs.urls')), `の部分では、  
   `http://127.0.0.1:8000/`にアクセサされた際に、`blogs.urls`ファイルを参照するように設定されています。  
   ※`blogs.url`ファイルはこの後作成する urls.py のことです。

   `path('blogs', include('blogs.urls)),`と書いた場合は、  
   `http://127.0.0.1:8000/blogs`にアクセスがあった場合、`blogs.urls`ファイルを参照するようになります。

   続いて、blogs アプリケーション内の URL 設定を行います。  
   django_blog/sblogs ディレクトリに移動し、`urls.py`ファイルを作成し、以下のコードを書く。

   ```
   from django.urls import path
   from . import views

   app_name = 'blogs'
   urlpatterns = [
      path('', views.index, name='index'),
   ]
   ```

   1 行目では Django の URL 機能である`path`関数をインポートしています。

   2 行目の`from . import views`の部分は、同じ階層にある`views.py`ファイルをインポートしています。  
   from の後に続いている`.`は同じ階層を意味しています。

   path 関数では、第一引数で空文字を指定し、第二引数で`views.index`を指定することで、  
   URL(http://127.0.0.1:8000/)へアクセスしたときは、views.pyのindex関数を実行するように設定している。

   例えば、path を`path('top', views.index, name='index')`のように設定すると、  
   URL(http://127.0.0.1:8000/top)へアクセスしたときに、index関数が実行されます。

   第三引数の`name='index'`では、URL パスに名前をつけています。

   ここまでで、ページを表示する準備が完了したので、`http://127.0.0.1:8000/`にアクセスすると、index.html で書いた内容が表示されるようになっています。
