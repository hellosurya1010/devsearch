from cProfile import Profile
from operator import mod
from re import L
from statistics import mode
from wsgiref.simple_server import demo_app
from django.db import models
from users.models import Profile
import uuid

# Create your models here.

class Project(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default="resibee.png")
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_totel = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    @property
    def calculateVoteRatio(self):
        reviews = self.review_set.all()
        upVotes = reviews.filter(value='up').count()
        totalVoutes = reviews.count()
        ratio = (upVotes / totalVoutes) * 100
        self.vote_ratio = ratio
        self.vote_totel = totalVoutes
        self.save()

    @property
    def revieweres(self):
        return self.review_set.all().values_list('owner__id', flat=True)

        

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']

class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, verbose_name="User") 
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        unique_together = [['owner', 'project']]

    def __str__(self):
        return self.value

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name


