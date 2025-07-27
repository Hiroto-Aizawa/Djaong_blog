from django.db import models

# Create your models here.
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