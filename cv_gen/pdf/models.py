from django.db import models
from users.models import User

# Create your models here.

class Profile(models.Model):

    author = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    summary = models.TextField(max_length=200)
    degree = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    total_experience = models.IntegerField(default=1)
    experience = models.TextField(max_length=1000)
    skills = models.TextField(max_length=1000)
    soft_skills = models.TextField(max_length=1000)


    def __str__(self):
        return self.name
    
