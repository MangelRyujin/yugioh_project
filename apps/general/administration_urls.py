from django.urls import path,include

from apps.general.views.dashboard_view import dashboard
from .views.home import home


urlpatterns = [
    
    path('', dashboard, name='dashboard'),   
    path('album/', include('apps.card.urls.album_urls')), 
    path('decks/', include('apps.card.urls.album_deck_urls')), 
    path('envios/', include('apps.order.urls.delivery_pakage_urls')), 
    path('nuevas-pedidos/', include('apps.order.urls.unpaid_order_urls')),
    path('pedidos-pagados/', include('apps.order.urls.paid_order_urls')),
]