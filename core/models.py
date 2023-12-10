from email.policy import default
from os import name
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    bio = models.TextField()
    location = models.CharField(max_length=255)
    profile_img = models.ImageField(upload_to='profilePics', default='profilePics/download.png')
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
    
    
class Posts(models.Model):
    img = models.ImageField(upload_to='posts')
    caption = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likesCount = models.IntegerField(default=0)
    def __str__(self):
        return self.user.username
    
    
class Likes(models.Model):
    likedPost = models.ForeignKey(Posts, on_delete=models.CASCADE)
    likedUser = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.likedUser.username
    
    
    
class Followers(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    
    def __str__(self):
        return ("Follower: " + self.follower.user.username + " " +"Following: " + self.following.user.username)
    
    
