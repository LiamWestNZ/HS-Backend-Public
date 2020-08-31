from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
User = settings.AUTH_USER_MODEL



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=220, null=True, blank=True)
    address2 = models.CharField(max_length=220, null=True, blank=True)
    city = models.CharField(max_length=220, null=True, blank=True)
    postal = models.CharField(max_length=220, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


def user_did_save(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)


post_save.connect(user_did_save, sender=User)