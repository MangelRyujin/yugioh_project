from django.urls import path

from apps.card.views.album_deck_view import album_deck


urlpatterns = [
    path('', album_deck, name='album_deck'),       
]