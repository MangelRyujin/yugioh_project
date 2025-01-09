from django.urls import path

from apps.card.views.album_view import album, add_card, search_cards_modal, search_user_cards



urlpatterns = [
    path('', album, name='album'),   
    path('search/', search_cards_modal, name='search_cards_modal'),
    path('search-user-cards/', search_user_cards, name='search_user_cards'),
    path('add-card/<int:pk>/', add_card, name='add_card'),
]