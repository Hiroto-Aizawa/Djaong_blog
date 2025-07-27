# ブログモデルを作ろう

## データベース（DB）とは？

## DB の作成

1. models.py に Blog モデルを作成する

   ```
   from django.db import models

   #インポートしたmodelsを使って、それを継承したBlogクラスを作成する
   # モデルを作成する際は「Blogs」のように複数形ではなく「Blog」のように単数形で作成する
   # これによって「Blogs」という名称のテーブルを自動生成してくれる
   class Blog(models.Model):
      title = models.CharField(blank=False, null=False, max_length=150)
      text = models.TextField()
      created_datetime = models.DateTimeField(auto_now_add=True)
      updated_datetime = models.DateTimeField(auto_now=True)

      def __str__(self):
         return self.title
   ```

   最後の`def __str__(self)`の部分は、このモデルで作成されたインスタンス（一つ一つのブログ記事）自体を指し示すときに利用する文字列を指定しています。  
   これによって、管理ページなどんで各インスタンスを表示するときは、ブログ記事のタイトルで表示されるようになります。  
   詳細については、[管理ページでブログを投稿する](#管理ページからブログを投稿する)で説明します。

## マイグレーション

1. マイグレート

   Blog モデルの作成はできましたが、現段階では実態がないため実際に DB を作成する必要があります  
   それが`マイグレート`という作業です。  
   マイグレートは、models.py ファイルで定義した DB の設計を、実際に DB に反映させることを言います。

   マイグレートするために、以下のコマンドを実行します。

   ```
   # マイグレーションファイルの作成
   (djangobros_venv) ~/DjangoBros/django_blog$ python3 manage.py makemigrations

   # 以下のように出力されればマイグレーションファイルが作成されています。
   Migrations for 'blogs':
      blogs/migrations/0001_initial.py
         - Create model Blog

   # マイグレーションファイルの情報をDBに反映させる
   (djangobros_venv) ~/DjangoBros/django_blog$ python3 manage.py migrate

   # 以下のように出力されればDBへの反映が完了しています。
   Operations to perform:
      Apply all migrations: admin, auth, blogs, contenttypes, sessions
   Running migrations:
      Applying blogs.0001_initial... OK

   ```

   `マイグレーションファイル`：models.py で作成した DB の設計情報がまとめられたファイル

   一連のコマンドで、models.py で作成した Blog モデルを DB に反映させることができました。  
   このように DB を作成する際は\*\*「models.py で設計 -> マイグレート処理で DB に反映」という手順で行います。  
   models.py に何か変更を加えた際は、その都度マイグレート処理を行い、変更内容を DB に反映させることを忘れないように注意が必要です。

## Admin ページを利用する

1. スーパーユーザーアカウントの作成

   ```
   (djangobros_venv) ~/DjangoBros/django_blog$ python3 manage.py createsuperuser
   ```

   上記コマンドを実行すると、  
    ・ユーザー名  
    ・メールアドレス  
    ・パスワード  
   の入力が求められるので、好きなように入力する。

   ユーザー名を何も入力せずに Enter を押すと、Ubuntu で設定しているユーザー名を自動的に使用します。

   管理者アカウントの作成が完了したら、  
   `http://127.0.0.1:8000/admin`にアクセスすることができます。

   ページに移動すると、ユーザー名とパスワードの入力が求められるので、先ほど設定したものを入力してください。

   次は、この Admin 画面で Blogs テーブルの情報を管理できるように設定してきます。  
   ※Admin ページが日本語表示されているのは、settings.py で`LANGUAGE_CODE = 'ja'`に設定しているためです。

1. Admin ページの編集

   Admin ページを編集するためには`admin.py`を開きます。  
   初めに、`admin.py`に Blog モデルを登録します。

   ```
   from django.contrib import admin
   from .models import Blog

   admin.site.register(Blog)
   ```

   2 行目の`from .models import Blog`は、admin.py と同じ階層にある`models.py`で定義した Blog モデルをインポートして、このファイル内で使用可能にしています。  
   ※`.`は同じ階層を意味しています。

   4 行目の`admin.site.register(blog)`の部分でインポートして Blog モデルを、Admin ページに登録し、使用できるようにしています。  
   `admin.py`を保存し、再度 Admin ページにアクセスすると、Blog の情報を見ることができます。

   Admin ページでは`Blogs`と表示されていますが、これは Blog モデルを作成すると自動的に複数形にしたテーブル（Blogs）が作成されたためです。

## 管理ページからブログを投稿する

1. Blogs の追加

   Blogs という欄の「追加」ボタンをクリックすると「Title」、「Text」の入力欄が表示されます。

   好きなようにタイトルと本文を入力し、「保存」ボタンで保存できます。
   これは、models.py で定義した Blog クラスのフィールド名が表示されています。  
   ここには文字列型のデータを入れられるように設定していました。

   タイトルを入力しないまま保存を押すと、エラーメッセージが表示されます。  
   Title フィールドは、`blank=False`を設定しているため、空のままでは入力できません。

   これで、Blog クラスをもとに Blog インスタンスを作成することができました。

   クラス：「オブジェクトを作成するための設計図」  
   インスタンス：「クラス（設計図）を元に作られたオブジェクト」

   テスト用にもう 1 つか 2 つ記事を投稿します。

1. def ＿str＿(self)について

   ここで、[DB の作成](#db-の作成)で説明した、`def __str__(self)`の説明をします。  
   ブログオブジェクトの一覧ページ(`http://127.0.0.1:8000/admin/blogs/blog`)では、それぞれのブログのタイトルが表示されています。  
   ここにタイトルが表示されているのは、以下のように`self.title`と記述しているからでうす。

   ```
   # django_blog/blogs/models.py

     ・・・
    def __str__(self):
        return self.title
   ```

   例えば、ここを`self.text`と書き換えると、ブログの本文が見出しとして表示されるようになります。  
   このように`def __self__(self)`の部分では、そのオブジェクトを扱う上で使用するフィールドを指定しています。

   また、現在はタイトルだけが表示されていますが、複数フィールドを表示させることもできます。 　
   以下のように、admin.py を編集してください。

   ```
   # django_blog/blogs/admin.py

   from django.contrib import admin
   from .models import Blog

   class BlogAdmin(admin.ModelAdmin):
      list_display = ('id', 'title', 'created_datetime', 'updated_datetime')
      list_display_links = ('id','title',)

   admin.site.register(Blog, BlogAdmin)
   ```

   `list_display`で指定したフィールドが管理ページに表示されています。  
   `list_display_links`で指定したフィールドはリンクがつくようになりました。

   ここで、BlogAdmin 関数の中で`id`という見慣れないフィールドが出てきました。  
   `ID`はインスタンスがデータベースに保存される際に自動的に割り振られる番号です。
   そのため、**models.py で定義していなくても、1 つのインスタンスに対して 1 つの ID が付与されます。**
