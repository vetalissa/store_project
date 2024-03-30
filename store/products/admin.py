from django.contrib import admin

from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
    fields = ('name', ('price', 'quantity'), 'description', 'category', 'image')
    search_fields = ('name', 'description')
    ordering = ('name', 'price')
