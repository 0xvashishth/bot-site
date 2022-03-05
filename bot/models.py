from sqlite3 import IntegrityError
from django.db import models

from statistics import mode
# Create your models here.

class user(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    phone = models.IntegerField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    Address = models.CharField(max_length=200)
    reason = models.CharField(max_length=1000)