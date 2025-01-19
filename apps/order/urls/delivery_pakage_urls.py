from django.urls import path
from apps.order.views.delivery_pakage_views import delivery_pakage

urlpatterns = [
    path('', delivery_pakage, name='delivery_pakage'), 
]