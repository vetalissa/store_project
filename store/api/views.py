from rest_framework.generics import ListAPIView

from products.serializers import ProductSerializer
from products.models import Product


class ProductListSerializer(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
