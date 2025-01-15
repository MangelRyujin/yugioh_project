from django.urls import path
from apps.order.views.unpaid_order_views import unpaid_order

urlpatterns = [
    path('', unpaid_order, name='unpaid_order'),    
       
]