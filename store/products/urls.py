from django.urls import path

from products.views import (BasketListView, ProductListView, basket_add,
                            basket_deleted, basket_down)

app_name = 'products'

urlpatterns = [
    path('catalog', ProductListView.as_view(), name='catalog'),
    path('category/<int:category_id>/', ProductListView.as_view(), name='category'),
    path('basket/<int:pk>/', BasketListView.as_view(), name='basket'),
    path('basket/add/<int:product_id>', basket_add, name='basket_add'),
    path('basket/down/<int:product_id>', basket_down, name='basket_down'),
    path('basket/deleted/<int:basket_id>', basket_deleted, name='basket_deleted'),
]
