from datetime import date
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=150)
    text = models.TextField()
    date_post = models.DateField(default=date.today)

    def __str__(self):
        return self.title

