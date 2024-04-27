from django.contrib import admin
from django.urls import include, path

from products.views import ProductListView

app_name = 'products'

urlpatterns = [
    path('catalog', ProductListView.as_view(), name='catalog'),
    path('category/<int:category_id>/', ProductListView.as_view(), name='category'),
]
