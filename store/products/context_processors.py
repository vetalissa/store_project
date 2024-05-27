from products.models import Basket


def baskets(request):
    user = request.user
    print()
    return {'baskets': Basket.object.filter(user=user) if user.is_authenticated else [],
            'basket_list': {i.product: i.quantity for i in Basket.object.filter(user=user)} if user.is_authenticated else []}
