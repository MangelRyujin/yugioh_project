from django.urls import path
from apps.order.views.delivery_pakage_views import delivery_pakage,delivery_pakage_edit

urlpatterns = [
    path('', delivery_pakage, name='delivery_pakage'), 
    path('<int:pk>/', delivery_pakage_edit, name='delivery_pakage_edit'), 
    
]