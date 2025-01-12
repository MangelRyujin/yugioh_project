from django.urls import path

from apps.general.views.pricing import pricing
from apps.general.views.dashboard_view import dashboard
from .views.home import home


urlpatterns = [
    path('', home, name='index'), 
    path('precios/', pricing, name='pricing'),
    
]