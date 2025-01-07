from django.urls import path

from apps.card.views.album_view import album



urlpatterns = [
    path('', album, name='album'),   
      
]