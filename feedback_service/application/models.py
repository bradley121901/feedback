from django.db import models

class ProductModel(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    