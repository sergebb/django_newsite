from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone
# Create your models here.

class TutorialGroup(models.Model):
    group_name = models.CharField(max_length=200)
    group_order = models.IntegerField()

    def __unicode__(self):              # __str__ on Python 3
        return self.group_name

class Tutorial(models.Model):
    tutorial_name = models.CharField(max_length=200)
    tutorial_order = models.IntegerField(blank=True)
    depend_on = models.ForeignKey('self',null=True,blank=True)
    tutorial_group = models.ForeignKey(TutorialGroup)

    def __unicode__(self):              # __str__ on Python 3
        return self.tutorial_name

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    picture = models.ImageField(upload_to='profile_images', blank=True)
    shell_login = models.CharField(max_length=200, blank=True)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=django.utils.timezone.now)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username