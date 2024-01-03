from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class User(AbstractBaseUser):
    username = models.CharField(max_length=200,null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)


