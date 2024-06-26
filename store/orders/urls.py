from django.urls import path

from orders.views import (CancelTemplateView, OrderCreateView, OrderDetailView,
                          OrderListView, SuccessTemplateView)

app_name = 'orders'

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='order_create'),
    path('success/', SuccessTemplateView.as_view(), name='order_success'),
    path('cancel/', CancelTemplateView.as_view(), name='order_cancel'),
    path('orders/', OrderListView.as_view(), name='orders'),
    path('order_detail/<int:pk>', OrderDetailView.as_view(), name='order_detail'),

]
