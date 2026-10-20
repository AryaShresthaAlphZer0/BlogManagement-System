from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)

class Blog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    def __str__(self):
        return self.title