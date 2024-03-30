from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from common.view import TitleMixin
from products.models import Product, ProductCategory


class ProductsView(TemplateView):
    template_name = 'products/products.html'


class ProductListView(TitleMixin, ListView):
    template_name = 'products/products.html'
    title = 'Католог'
    model = Product
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data()
        context['categories'] = ProductCategory.objects.all()
        return context

    def get_queryset(self):
        queryset = super(ProductListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')

        return queryset.filter(category_id=category_id) if category_id else queryset
