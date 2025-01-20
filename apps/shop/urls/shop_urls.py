
from django.urls import path
from apps.shop.views import shop_view, search_cards

urlpatterns = [
    path('', shop_view, name='shop'),
    path('search-card/', search_cards, name='search_cards_shop'),
]
