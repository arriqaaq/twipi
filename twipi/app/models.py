from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
     user = models.OneToOneField(User)
     followers = models.ManyToManyField('self', related_name='follows', symmetrical=False)

     # Override the __unicode__() method to return out something meaningful!
     def __unicode__(self):
         return self.user.username


class Tweet(models.Model):
	
     text=models.CharField(max_length=140)
     user=models.ForeignKey(User)
     time=models.DateTimeField(auto_now=True)
     def __unicode__(self):
         return self.text

class Replies(models.Model):
     created = models.DateTimeField(auto_now=True)
     author = models.CharField(max_length=60)
     text=models.CharField(max_length=140)
     tweet=models.ForeignKey(Tweet)

