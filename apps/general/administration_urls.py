from django.urls import path,include

from apps.general.views.dashboard_view import dashboard
from .views.home import home


urlpatterns = [
    
    path('', dashboard, name='dashboard'),   
    path('album/', include('apps.card.urls.album_urls')), 
    path('envios/', include('apps.order.urls.order_urls')), 
]