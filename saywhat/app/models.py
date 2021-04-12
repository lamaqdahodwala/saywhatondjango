from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    upvotes = models.IntegerField()
    upvotes.default = 0
    def __str__(self):
        return self.title + ' | ' + str(self.author)
