
from django.urls import path
from apps.shop.views import shop_view

urlpatterns = [
    path('', shop_view, name='shop'),
]
