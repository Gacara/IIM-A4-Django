import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    message = models.TextField(max_length=400)
    pub_date = models.DateTimeField(auto_now=True)
    cv_Img = models.ImageField(upload_to='images/') 

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Skills: {self.message}"
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)