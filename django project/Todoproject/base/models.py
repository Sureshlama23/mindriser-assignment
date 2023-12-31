from django.db import models

# Create your models here.
class Todoproject(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    status = models.CharField(max_length =50,choices=[('Done','Done'),('In progress', 'In progress'), ('Not done','Not done')])

    def __str__(self) -> str:
        return self.name
        