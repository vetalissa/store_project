from django.db import models

from products.models import Basket, Product
from users.models import User


class Order(models.Model):
    CREATED = 0
    PAID = 1
    ON_WAY = 2
    DELIVERED = 3

    STATUSES = (
        (CREATED, 'Создан'),
        (PAID, 'Оплачен'),
        (ON_WAY, 'В пути'),
        (DELIVERED, 'Доставлен'),
    )

    initiator = models.ForeignKey(to=User, on_delete=models.CASCADE)
    address = models.TextField(max_length=300)
    date_create = models.DateTimeField(auto_now=True)
    status = models.PositiveSmallIntegerField(default=CREATED, choices=STATUSES)
    basket_history = models.JSONField(default=dict)

    def __str__(self):
        return f'Заказ #{self.id}. {self.initiator}'

    def order_update_after_payment(self):
        baskets = Basket.object.filter(user=self.initiator)
        self.change_count(baskets)
        self.status = self.PAID
        self.basket_history = {
            'purchased_items': [basket.de_json() for basket in baskets],
            'total_sum': float(baskets.total_sum())
        }
        baskets.delete()
        self.save()

    @staticmethod
    def change_count(basket):
        for product_in_basket in basket:
            count = product_in_basket.quantity
            product = Product.objects.get(id=product_in_basket.product.id)
            product.quantity -= count
            product.save()
