from django.db import models
from management.models import Room

# Create your models here.

class GuestInfo(models.Model):
    name = models.CharField(max_length=100)
    Phone_no = models.IntegerField()
    address = models.TextField()
    email = models.EmailField(unique=True)

class GuestRoom(models.Model):
    guest = models.ForeignKey(GuestInfo,on_delete=models.SET_NULL,null=True)
    room = models.ForeignKey(Room,on_delete=models.SET_NULL,null=True)

