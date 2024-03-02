from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group

# Create your models here.
class User(AbstractUser,BaseModel):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
 