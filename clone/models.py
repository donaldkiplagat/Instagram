from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models import Q

import datetime as dt

Gender=(
    ('Male','Male'),
    ('Female','Female'),
)
# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.location

    class Meta:
        ordering = ['location']

    def save_location(self):
        self.save()

    @classmethod
    def delete_location(cls,location):
        cls.objects.filter(location=location).delete()

class Post(models.Model):
    profile_pic = models.ImageField(upload_to = 'profilepics/')
    caption = models.CharField(max_length=3000)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ImageField(upload_to='posts/')
    likes = models.IntegerField()

    location = models.ForeignKey(Location,on_delete=models.CASCADE)

    post_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='profilepics/')
    bio = HTMLField()
    name = models.CharField(max_length=255)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    email= models.EmailField()
    phonenumber = models.IntegerField()
    gender = models.CharField(max_length=15,choices=Gender,default="Male")

    def __str__(self):
        return self.username

    @classmethod
    def search_profile(cls,search_term):
        profiles = cls.objects.filter(Q(username__username=search_term) | Q(name__icontains=search_term))

        return profiles

class Comment(models.Model):
    comment = models.CharField(max_length=300)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    # post = models.ForeignKey(Post,on_delete=models.CASCADE)
    post = models.IntegerField()

    def save_comment(self):
        self.save()

    # @classmethod
    # def delete_comment(self):
    #     self.delete()
    #
class Followers(models.Model):
    username= models.ForeignKey(User,on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
