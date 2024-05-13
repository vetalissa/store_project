from django.db import models

from users.models import User
from django import template

register = template.Library()


class ProductCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products_image')
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=50, decimal_places=2)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)

    # def product_in(self, product_id):
    #     return True if self.object.filter(product_id=product_id) else False


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    object = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт: {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity

    @classmethod
    def create_or_update(cls, product_id, user):
        basket = Basket.object.filter(user=user, product_id=product_id)

        if not basket.exists():
            Basket.object.create(user=user, product_id=product_id, quantity=1)
        else:
            basket = basket.first()
            basket.quantity += 1
            basket.save()

    @classmethod
    def down_quantity(cls, product_id, user):
        basket = Basket.object.filter(user=user, product_id=product_id)

        if basket.first().quantity - 1 == 0:
            basket.delete()
        else:
            basket = basket.first()
            basket.quantity -= 1
            basket.save()
