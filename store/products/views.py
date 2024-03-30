from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from common.view import TitleMixin
from products.models import Product


class ProductsView(TemplateView):
    template_name = 'products/products.html'


class ProductListView(TitleMixin, ListView):
    template_name = 'products/products.html'
    title = 'Католог'
    model = Product
    queryset = Product.objects.all()
    paginate_by = 3
