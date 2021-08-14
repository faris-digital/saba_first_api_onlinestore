from django.db import models
from django.db.models.deletion import CASCADE


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)


class Product(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=CASCADE, related_name="products"
    )
    description = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    shipping_cost = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.SmallIntegerField()
