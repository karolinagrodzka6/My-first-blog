from django.db import models
from django.utils import timezone
from django.contrib import admin

class Tag(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, default='')

    def __str__(self):
        return self.name

class User (models.Model) :
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def login (self) :
        return self.username

class comment (models.Model):
    author = models.CharField(max_length=200)
    text = models.CharField(max_length=500)
    published_date = models.DateTimeField(
        blank=True, null=True)

class Post(models.Model):

    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


