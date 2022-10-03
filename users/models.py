import email
from email.policy import default
from operator import mod
from xml.parsers.expat import model
from django.db import models
from django.contrib.auth.models import User
import uuid

from django.forms import CharField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, null=True, blank=True)
    username = models.CharField(max_length=256, null=True, blank=True)
    location = models.CharField(max_length=256, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    short_intro = models.CharField(max_length=254, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(upload_to="profiles", null=True, blank=True, default="profiles/profile.png")
    social_linkedin = models.CharField(max_length=256, null=True, blank=True)
    social_youtube = models.CharField(max_length=256, null=True, blank=True)
    social_github = models.CharField(max_length=256, null=True, blank=True)
    social_twitter = models.CharField(max_length=256, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.user.username)

class Skill(models.Model):        
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)