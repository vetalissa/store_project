from django.contrib import admin

from orders.models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status')
    fields = (
        'id', 'date_create',
        'initiator',
        'address',
        'basket_history', 'status',
    )
    readonly_fields = ('id', 'date_create')

