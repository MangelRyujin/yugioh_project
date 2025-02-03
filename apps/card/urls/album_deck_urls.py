from django.urls import path

from apps.card.views.album_deck_view import *


urlpatterns = [
    path('', album_deck, name='album_deck'),
    path('search-deck/', search_album_deck, name='search_album_deck'),    
    path('add-card/', create_album_deck, name='create_album_deck'), 
    path('delete-deck/<int:pk>/', delete_album_deck, name='delete_album_deck'),     
      
]