from django.db import models

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
