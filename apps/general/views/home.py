from django.shortcuts import render

from apps.card.models import AlbumCard,AlbumDecks

# Create your views here.

def home(request):
    context={
        'tota_cards': AlbumCard.objects.all().count(),
        'tota_decks': AlbumDecks.objects.all().count()
    }
    return render(request,'index.html',context)
