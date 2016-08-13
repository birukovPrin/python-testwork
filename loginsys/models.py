from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core import validators
from django.core.validators import RegexValidator


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,11}$', message="Phone number must be entered in the format: '+999999999'")
    phone = models.CharField(max_length=11, validators=[phone_regex], blank=True, null=True)

    skype = models.CharField(validators=[validators.validate_slug], max_length=30, blank=True, null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
