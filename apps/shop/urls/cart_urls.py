
from django.urls import path
from apps.shop.views.cart_view import *
from apps.shop.views.cart_instance_view import clear_cart_instance,album_card_detail_shop_card,add_to_cart_instance,cart_view, remove_to_cart_instance, increment_cart_item, decrement_cart_item, remove_cart_item, check_cart

urlpatterns = [
    #path('', cart_view, name='cart_view'),
    path('add/<int:content_type_id>/<int:object_id>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:content_type_id>/<int:object_id>/', remove_from_cart, name='remove_from_cart'),
    # path('clear/', clear_cart, name='clear_cart'),
    path('increase/<int:content_type_id>/<int:object_id>/', increase_quantity, name='increase_quantity'),
    path('decrease/<int:content_type_id>/<int:object_id>/', decrease_quantity, name='decrease_quantity'),
    path('cart/', cart_detail, name='cart_detail'),
    
    # Example cart instance
    path('', cart_view, name='cart_view'),
    path('album_card_detail_shop_card/<int:pk>/', album_card_detail_shop_card, name='album_card_detail_shop_card'),
    path('add_to_cart_instance/<int:pk>/<str:object>', add_to_cart_instance, name='add_to_cart_instance'),
    path('remove_to_cart_instance/<int:pk>/<str:object>', remove_to_cart_instance, name='remove_to_cart_instance'),
    path('increment_cart_item/<int:pk>/<str:object>/', increment_cart_item, name='increment_cart_item'),
    path('decrement_cart_item/<int:pk>/<str:object>/', decrement_cart_item, name='decrement_cart_item'),
    path('remove_cart_item/<int:pk>/<str:object>/', remove_cart_item, name='remove_cart_item'),
    path('clear_cart_instance/', clear_cart_instance, name='clear_cart_instance'),
    path('check_cart/', check_cart, name='check_cart'),
    
]
