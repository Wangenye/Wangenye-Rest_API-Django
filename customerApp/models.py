from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class  UserProfile(models.Model):
    user = models.OneToOneField(User,related_name= 'userprofile',on_delete=models.CASCADE)
    phone = models.CharField(max_length=13, blank=True)
    
    @receiver(post_save, sender=User)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)