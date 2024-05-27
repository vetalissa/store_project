from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from common.view import EmailAgainSendMixin, TitleMixin
from products.models import Basket, Product, ProductCategory


class ProductListView(TitleMixin, ListView):
    template_name = 'products/products.html'
    title = 'Каталог'
    model = Product
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data()
        context['categories'] = ProductCategory.objects.all()
        return context

    def get_queryset(self):
        queryset = super(ProductListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')

        return queryset.filter(category_id=category_id) if category_id else queryset


class ProductDetailView(DetailView):
    template_name = 'products/one_product.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = self.object.name
        return context


class BasketListView(TitleMixin, EmailAgainSendMixin, TemplateView):
    template_name = 'products/basket.html'
    title = 'Корзина'


@login_required
def basket_add(request, product_id):
    Basket.create_or_update(product_id=product_id, user=request.user)

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_down(request, product_id):
    Basket.down_quantity(product_id=product_id, user=request.user)

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_deleted(request, basket_id):
    basket = Basket.object.get(id=basket_id)
    basket.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
