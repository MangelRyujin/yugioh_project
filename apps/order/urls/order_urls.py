from django.urls import path
from apps.order.views.order_view import order
from apps.order.views.unpaid_order_views import unpaid_order

urlpatterns = [
    path('', order, name='order'), 
]