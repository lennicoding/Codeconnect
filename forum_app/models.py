from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Post(models.Model):
    vote_count = models.IntegerField(default=0)
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateField(default=date.today)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    tags = models.ManyToManyField('Tag', related_name='posts')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Post Author', default="")

    def __str__(self):
        return str(self.id) + ' ' + self.title


class Tag(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Answer(models.Model):
    answer = models.CharField(max_length=1000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='answers')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Answer Author', default="")

    def __str__(self):
        return self.answer

