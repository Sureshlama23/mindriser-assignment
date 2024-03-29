from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100,unique=True)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    ISBN = models.CharField(max_length=50,unique=True)
    description = models.TextField()
    file = models.FileField(null=True, blank=True)