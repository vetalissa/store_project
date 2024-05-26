from django.urls import path

from api.views import ProductListSerializer

app_name = 'api'

urlpatterns = [
    path('list-view/', ProductListSerializer.as_view(), name='list-view'),
]
