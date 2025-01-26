
from django.urls import path
from apps.shop.views.card_view import *

urlpatterns = [
    path('', shop, name='shop'),
    path('card/', shop_card, name='shop_card'),
    path('card-search-results/', cards_search_result, name='cards_search_result'),
    path('card-filter-results/', cards_filter_result, name='cards_filter_result'),
    
]
