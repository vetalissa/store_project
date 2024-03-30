from django.contrib import admin
from django.urls import include, path

from products.views import ProductListView

app_name = 'products'

urlpatterns = [
    path('product-view', ProductListView.as_view(), name='catalog'),
]
