from django.contrib import admin

from products.models import Basket, Product, ProductCategory


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
    fields = ('name', ('price', 'quantity'), 'description', 'category', 'stripe_product_price_id', 'image')
    search_fields = ('name', 'description')
    ordering = ('name', 'price')


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name', 'description')


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
