from django.urls import path

from apps.general.views.dashboard_view import dashboard
from .views.home import home


urlpatterns = [
    path('', home, name='index'),   
    path('administración/', dashboard, name='dashboard'),   
]