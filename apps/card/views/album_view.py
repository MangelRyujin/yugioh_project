from django.shortcuts import render
from apps.card.models import *
import requests
from django.http import  HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.card.models import AlbumCard, Album
import requests
from django.http import HttpResponse
# Create your views here.


@login_required
def search_user_cards(request):
    if request.method == 'POST':
        query = request.POST.get('kbdInput2', '')
        #print(f"Query: {query}")  # Agrega esta línea para depurar
        if not query:
            print("No se recibió ningún valor para 'kbdInput'")
        user_album = Album.objects.get(user=request.user)
        album_cards = AlbumCard.objects.filter(album=user_album, card__name__icontains=query, stock__gt=0)
        
        context = {
            'cards': album_cards,
        }
        
        #print(f"Primer objeto de album_cards: {album_cards.first().card.name}")
        #print(album_cards.first().card.name)
        # imprime por consola el primer objeto de album_cards
        
        
        return render(request, 'components/album/card_list.html', context)
    return HttpResponse('<p>Método no permitido</p>', status=405)

def search_cards_modal(request):
    if request.method == 'POST':
        #print(request.POST.get('kbdInput'))
        query = request.POST.get('kbdInput1', '')
        external_api_url = f'https://primervirgen.pythonanywhere.com/api/cards/?name={query}'
        #print(f"Query: {query}")  # Agrega esta línea para depurar
        
        try:
            response = requests.get(external_api_url)
            if response.status_code == 200:
                data = response.json()
                #print(f"URL: {external_api_url}")  # Agrega esta línea para depurar
                return render(request, 'components/album/add_card_modal/search_results.html', {'cards': data['results']})
            else:
                return HttpResponse('<p>No se encontraron resultados</p>', status=response.status_code)
        except requests.exceptions.RequestException as e:
            return HttpResponse(f'<p>Error: {str(e)}</p>', status=500)
    return HttpResponse('<p>Método no permitido</p>', status=405)

def album(request):
    #context={'list':[0,1,3,4,56,7,8,9,12,4112,41,0,1,3,4,56,7,8,9,12,4112,41,0,1,3,4,56,7,8,9,12,4112,41]}
    #external_api_url = 'https://primervirgen.pythonanywhere.com/api/cards/?konami_id=33656832'
    
    
    user_album = Album.objects.get(user=request.user)
    album_cards = AlbumCard.objects.filter(album=user_album, stock__gt=0)
    
    
    context = {
        'cards': album_cards,
    }
    
    return render(request,'dashboard/album/index.html', context)



def add_card(request,pk:int):
    pass