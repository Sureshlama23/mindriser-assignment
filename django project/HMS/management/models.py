from django.db import models
from user.models import User

# Create your models here.

class Room(models.Model):
    room_no = models.CharField(max_length=200)
    floor = models.CharField(max_length=200)
    description = models.TextField()
    type = models.ForeignKey('RoomType',on_delete=models.SET_NULL,null=True)


class RoomType(models.Model):
    name = models.CharField(max_length=200)

class EmployeeInfo(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField()
    photo = models.ImageField(upload_to='Employee_image')
    user = models.OneToOneField(User,on_delete=models.CASCADE)
