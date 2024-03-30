from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products_image')
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=50, decimal_places=2)
