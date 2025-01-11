from django.urls import path

from apps.card.views.album_card import album_card_form_update, album_card_update
from apps.card.views.album_view import album, add_card, album_card_delete, search_cards_modal, search_user_cards



urlpatterns = [
    path('', album, name='album'),   
    path('search/', search_cards_modal, name='search_cards_modal'),
    path('search-user-cards/', search_user_cards, name='search_user_cards'),
    path('add-card/<int:pk>/', add_card, name='add_card'),
    path('delete-card/<int:pk>/', album_card_delete, name='album_card_delete'),
    path('editar-carta/<int:pk>/', album_card_update, name='album_card_update'),
    path('formulario-editar-carta/<int:pk>/', album_card_form_update, name='album_card_form_update'),
    
    
    
]