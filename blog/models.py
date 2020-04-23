from django.db import models
from django.conterib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(defalt=timezone)

    def__str__(self):
       return self.title 
