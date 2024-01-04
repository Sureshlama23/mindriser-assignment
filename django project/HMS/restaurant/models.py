from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

class Food(models.Model):
    name = models.CharField(max_length=200)
    menu = models.ForeignKey(Menu,on_delete=models.SET_NULL,null=True)
    

