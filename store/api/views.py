from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from products.models import Basket, Product
from products.serializers import BasketSerializer, ProductSerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action in ('create', 'update', 'destroy'):
            self.permission_classes = (IsAdminUser,)
        return super(ProductModelViewSet, self).get_permissions()


class BasketModelViewSet(ModelViewSet):
    queryset = Basket.object.all()
    serializer_class = BasketSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None

    def get_queryset(self):
        queryset = super(BasketModelViewSet, self).get_queryset()
        return queryset.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        try:
            product_id = request.data['product_id']
            products = Product.objects.filter(id=product_id)
            if not products.exists():
                return Response({'product_id': 'not found this id'}, status=status.HTTP_400_BAD_REQUEST)
            obj, is_created = Basket.create_or_update(products.first().id, self.request.user)
            if obj:
                status_code = status.HTTP_201_CREATED if is_created else status.HTTP_200_OK
                serializer = self.get_serializer(obj)
                return Response(serializer.data, status=status_code)
            else:
                return Response({'ErrorQuantity': 'Is product max quantity'}, status=status.HTTP_409_CONFLICT)

        except KeyError:
            return Response({'product_id': 'This field is required'}, status=status.HTTP_400_BAD_REQUEST)
