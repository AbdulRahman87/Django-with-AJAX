from pyexpat import model
from django.db import models

# Create your models here.

class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15, default='User')
    phno = models.IntegerField()
    age = models.IntegerField()

    def __str__(self):
        return self.name