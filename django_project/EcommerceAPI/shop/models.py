from django.db import models
from base.models import BaseModel
from user.models import User

# Create your models here.

class shopDetail(BaseModel):
    user = models.ForeignKey(User,on_delete=models.PROTECT,related_name='shopdetatils')
    name = models.CharField(max_length=100,unique=True)
    number = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return f"{(self.user.username),(self.name)}"
    


