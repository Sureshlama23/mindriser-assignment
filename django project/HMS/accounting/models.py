from django.db import models
from frontdesk.models import GuestInfo

# Create your models here.

class Bill(models.Model):
    guest = models.ForeignKey(GuestInfo,on_delete=models.SET_NULL,null=True)
    amount = models.IntegerField()

class Payment(models.Model):
    bill = models.OneToOneField(Bill,on_delete=models.SET_NULL,null=True)
    paid_amount = models.IntegerField()