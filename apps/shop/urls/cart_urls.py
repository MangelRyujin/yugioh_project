
from django.urls import path
from apps.shop.views.cart_view import *

urlpatterns = [
    #path('', cart_view, name='cart_view'),
    path('add/<int:content_type_id>/<int:object_id>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:content_type_id>/<int:object_id>/', remove_from_cart, name='remove_from_cart'),
    path('clear/', clear_cart, name='clear_cart'),
    path('increase/<int:content_type_id>/<int:object_id>/', increase_quantity, name='increase_quantity'),
    path('decrease/<int:content_type_id>/<int:object_id>/', decrease_quantity, name='decrease_quantity'),
    path('cart/', cart_detail, name='cart_detail'),
]
