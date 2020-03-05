from django.db import models
from django import forms

# Create your models here.

class signup(models.Model):
    fullname = models.TextField()
    email = models.EmailField()
    username = models.TextField()
    password = models.TextField()

class login(models.Model):
    user = models.TextField()
    password = models.TextField()

