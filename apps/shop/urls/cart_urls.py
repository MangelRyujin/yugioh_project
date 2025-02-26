
from django.urls import path
from apps.shop.views.cart_view import *

urlpatterns = [
    path('', cart_view, name='cart_view'),
    
]
