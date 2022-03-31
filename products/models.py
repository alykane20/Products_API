from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory_quantity = models.IntegerField()

    