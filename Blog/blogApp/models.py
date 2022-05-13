import time

from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    content = models.TextField()
    author = models.CharField(max_length=40)
    publishedAt = models.DateTimeField(default=timezone.now)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
