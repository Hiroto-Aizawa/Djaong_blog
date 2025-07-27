# ブログモデルを作ろう

## データベース（DB）とは？

## DB の作成

## マイグレーション

1. マイグレート

   Blog モデルの作成はできましたが、現段階では実態がないため実際に DB を作成する必要があります  
   それが`マイグレート`という作業です。  
   マイグレートは、models.py ファイルで定義した DB の設計を、実際に DB に反映させることを言います。

   マイグレートするために、以下のコマンドを実行します。

   ```
   # マイグレーションファイルの作成
   (djangobros_venv) ~/DjangoBros/django_blog$ python3 manage.py makemigrations

   # マイグレーションファイルの情報をDBに反映させる
   (djangobros_venv) ~/DjangoBros/django_blog$ python3 manage.py migrate

   ```

   `マイグレーションファイル`：models.py で作成した DB の設計情報がまとめられたファイル

   一連のコマンドで、models.py で作成した Blog モデルを DB に反映させることができました。  
   このように DB を作成する際は\*\*「models.py で設計 -> マイグレート処理で DB に反映」という手順で行います。  
   models.py に何か変更を加えた際は、その都度マイグレート処理を行い、変更内容を DB に反映させることを忘れないように注意が必要です。

## Admin ページを利用する

## 管理ページからブログを投稿する
