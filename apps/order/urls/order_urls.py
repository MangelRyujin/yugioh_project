from django.urls import path
from apps.order.views.order_view import order

urlpatterns = [
    path('', order, name='order'),       
]