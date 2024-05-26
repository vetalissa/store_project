from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from home.views import HomeView
from orders.views import stripe_webhook_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('products/', include('products.urls', namespace='products')),
    path('users/', include('users.urls', namespace='users')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('accounts/', include('allauth.urls')),
    path('webhook/stripe/', stripe_webhook_view, name='stripe_webhook'),
    path('api/', include('api.urls', namespace='api')),

]

if settings.DEBUG:
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
