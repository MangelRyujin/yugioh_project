from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:content_type_id>/<int:object_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:content_type_id>/<int:object_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('clear/', views.clear_cart, name='clear_cart'),
    path('increase/<int:content_type_id>/<int:object_id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease/<int:content_type_id>/<int:object_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('cart/', views.cart_detail, name='cart_detail'),
]