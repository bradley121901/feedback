from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=25)
    price=models.CharField(max_length=25)
    description=models.CharField(max_length=1000)