from django.urls import path, include

from apps.general.views.pricing import pricing
from apps.general.views.dashboard_view import dashboard
from .views.home import home


urlpatterns = [
    path('', home, name='index'), 
    path('precios/', pricing, name='pricing'),
    path('tienda/', include('apps.shop.urls.shop_urls')),
    path('carrito/', include('apps.shop.urls.cart_urls')),  # incluye las urls del carrito de compras
    path('mi_compra/', include('apps.shop.urls.cart_urls')),
    
]