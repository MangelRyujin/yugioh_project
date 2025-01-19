from django.urls import path
from apps.order.views.paid_order_views import paid_order

urlpatterns = [
    path('', paid_order, name='paid_order'),    
       
]