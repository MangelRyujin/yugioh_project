
from django.urls import path
from apps.shop.views.card_view import *
from apps.shop.views.deck_view import *

urlpatterns = [
    path('', shop, name='shop'),
    #Cards
    path('card/', shop_card, name='shop_card'),
    path('card-search-results/', cards_search_result, name='cards_search_result'),
    path('card-filter-results/', cards_filter_result, name='cards_filter_result'),
    #Decks
    path('deck/', shop_deck, name='shop_deck'),
    path('deck-search-results/', decks_search_result, name='decks_search_result'),
    path('deck/<int:pk>', shop_deck_card, name='shop_deck_card'),
    path('deck-card-search/<int:pk>', shop_deck_cards_search_result, name='shop_deck_cards_search_result'),
]
