from django.db import models
from user.models import User
from base.models import BaseModel
from autoslug import AutoSlugField
# Create your models here.

ZONE_CHOICES = (
    ('Mahakali','Mahakali'),
    ('Seti','Seti'),
    ('Bheri','Bheri'),
    ('Karnali','Karnali'),
    ('Rapti','Rapti'),
    ('Dhawalagiri','Dhawalagiri'),
    ('Lumbini','Lumbini'),
    ('Gandaki','Gandaki'),
    ('Bagmati','Bagmati'),
    ('Narayani','Narayani'),
    ('Janakpur','Janakpur'),
    ('Sagarmatha','Sagarmatha'),
    ('Koshi','Koshi'),
    ('Mechi','Mechi'),
)

class Customer(BaseModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_customer')
    customer_name = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.PositiveIntegerField()
    zone = models.CharField(choices=ZONE_CHOICES,max_length=100)
    number = models.CharField(max_length=15)
    customer_slug = AutoSlugField(populate_from='customer_name',unique=True,null=True,blank=True)

    def __str__(self):
        return self.customer_name
