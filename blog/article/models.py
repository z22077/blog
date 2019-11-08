from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=128, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=128)

    def __str__(self):
        return self.article.title + '-' + str(self.id)