from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    ISBN = models.CharField(max_length=50,unique=True)
    description = models.TextField()
    file = models.FileField(upload_to='static/bookspdf/',null=True)
