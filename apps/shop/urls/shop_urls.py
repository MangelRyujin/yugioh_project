
from django.urls import path
from apps.shop.views import shop_view, search_cards, apply_filters

urlpatterns = [
    path('', shop_view, name='shop'),
    path('search-card/', search_cards, name='search_cards_shop'),
    path('apply-filters/', apply_filters, name='apply_filters'),
]
