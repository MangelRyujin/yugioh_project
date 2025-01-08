from django.urls import path

from apps.card.views.album_view import album, search_cards, add_card



urlpatterns = [
    path('', album, name='album'),   
    path('search/', search_cards, name='search_cards'),
    path('add-card/', add_card, name='add_card'),
]