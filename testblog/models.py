from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core import validators

class Post(models.Model):

    username = models.CharField(max_length=50,default="guest")
    title = models.CharField(validators=[validators.validate_slug], max_length=50)
    text = models.TextField()
    date = models.DateTimeField(
            default=timezone.now)


class Comments(models.Model):

    text = models.TextField()
    username = models.CharField(max_length=50)
    article = models.ForeignKey(Post, related_query_name="article")
