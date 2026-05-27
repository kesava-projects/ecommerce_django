from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    category = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.DecimalField(max_digits=5, decimal_places=2)

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    prod_id = models.IntegerField()
    prod_name = models.CharField(max_length=100)
    prod_price = models.DecimalField(max_digits=10, decimal_places=2)
