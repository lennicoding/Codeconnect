from django.db import models
from datetime import date

class Post(models.Model):
    vote_count = models.IntegerField(default=0)
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateField(default=date.today)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    tags = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id) + ' ' + self.title

class Tag(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name
