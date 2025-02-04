from django.urls import path

from apps.card.views.album_deck_card import *
from apps.card.views.album_deck_view import *


urlpatterns = [
    path('', album_deck, name='album_deck'),
    path('search-deck-cards/<int:pk>/', search_deck_user_cards, name='search_deck_user_cards'),
    path('album-deck-detail/<int:pk>/', album_deck_detail, name='album_deck_detail'),
    path('search-deck/', search_album_deck, name='search_album_deck'),    
    path('add-deck/', create_album_deck, name='create_album_deck'), 
    path('add-deck-card/<int:pk>', add_deck_card, name='add_deck_card'), 
    path('delete-deck/<int:pk>/', delete_album_deck, name='delete_album_deck'),     
    path('update-deck-card/<int:pk>/', album_deck_card_update, name='album_deck_card_update'),
    path('update-deck-card-form/<int:pk>/', album_deck_card_form_update, name='album_deck_card_form_update'),
    path('delete-deck-card/<int:pk>/', album_deck_card_delete, name='album_deck_card_delete'), 
    path('search-deck-card-add/', search_deck_cards_modal, name='search_deck_cards_modal'),
    path('update-deck-profile/<int:pk>/', update_deck_profile, name='update_deck_profile'),
    
]