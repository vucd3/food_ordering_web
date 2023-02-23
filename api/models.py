from django.db import models

# Create your models here.
class Food(models.Model):
    user = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    price = models.CharField(max_length=1000)
    quantity = models.IntegerField()

class User(models.Model):
    name = models.CharField(max_length=1000)
    passwd = models.CharField(max_length=1000)