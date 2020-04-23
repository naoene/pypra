from django.db import models

# Create your models here.
from django.db import models


class question(models.model):
    question_text = models.ChaField(max_length=200)
    pub_date = models.DateTimeField('date published')


class choice(models.model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)