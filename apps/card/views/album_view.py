from django.shortcuts import render, get_object_or_404
from apps.card.models import AlbumCard, Album
import requests
from rest_framework import status, response
from django.http import JsonResponse, HttpResponse

# Create your views here.

def search_cards(request):
    if request.method == 'POST':
        #print(request.POST.get('kbdInput'))
        query = request.POST.get('kbdInput', '')
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


def add_card(request):
    if request.method == 'POST':
        konami_id = request.POST.get('konami_id', '')
        
        if not konami_id:
            return JsonResponse({'error': 'konami_id es requerido'}, status=400)
        
        user_album = get_object_or_404(Album, user=request.user)
        
        new_album_card = AlbumCard(
            konami_id=konami_id,
            album=user_album
        )
        
        new_album_card.save()
        
        album_cards = AlbumCard.objects.filter(album=user_album, stock__gt=0)
        
        context = {
            'cards': album_cards,
        }
        
        return render(request, 'dashboard/album/index.html', context)
    
    return HttpResponse('<p>Método no permitido</p>', status=405)