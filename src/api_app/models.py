from django.db import models

# Create your models here.v

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=1500)


class Tag(models.Model):
    name = models.CharField(max_length=100)
    posts = models.ManyToManyField(Post)