from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=45)
    category = models.CharField(max_length=45)
    stock = models.IntegerField(default=True)
    price = models.IntegerField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)