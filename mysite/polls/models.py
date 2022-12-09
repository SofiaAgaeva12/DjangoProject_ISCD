import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class AuthUser(AbstractUser):
    avatar = models.ImageField(upload_to='polls/media/avatars', blank=False)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    question_votes = models.IntegerField(default=0)
    description = models.TextField(max_length=600)

    image = models.ImageField(upload_to='polls/media/questions')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    def get_percentage(self):
        percents = round(self.votes * 100 / self.question.question_votes, 2)
        return percents

class Vote(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
