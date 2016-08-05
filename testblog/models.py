from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):

    username = models.CharField(max_length=50,default="guest")
    title = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateTimeField(
            default=timezone.now)
