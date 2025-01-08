from django.shortcuts import render, get_object_or_404
from apps.card.models import *
import requests
from rest_framework import status, response
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required

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


from django.shortcuts import render, get_object_or_404
from apps.card.models import AlbumCard, Album, Card, CardSet, CardImage, CardPrice
import requests
from django.http import JsonResponse, HttpResponse

def add_card(request):
    if request.method == 'POST':
        konami_id = request.POST.get('konami_id', '')
        
        if not konami_id:
            return JsonResponse({'error': 'konami_id es requerido'}, status=400)
        
        # enlace de la peticion
        external_api_url = f'https://primervirgen.pythonanywhere.com/api/cards/?konami_id={konami_id}'
        
        # response para almacenar los datos de la carta
        response = requests.get(external_api_url)
        if response.status_code == 200:
            data = response.json()['results'][0]
            
            user_album = get_object_or_404(Album, user=request.user)
            
            exists_album_card = AlbumCard.objects.filter(konami_id=konami_id).first()
            if exists_album_card:    
                exists_album_card.stock += 1
                exists_album_card.save()
            else:
                new_album_card = AlbumCard(
                    konami_id=konami_id,
                    album=user_album
                )
                
                new_album_card.save()
                
                # Crear instancia de Card
                card = Card.objects.create(
                    konami_id=data['konami_id'],
                    name=data['name'],
                    typeline=data['typeline'],
                    type=data['type'],
                    humanReadableCardType=data['humanReadableCardType'],
                    frameType=data['frameType'],
                    desc=data['desc'],
                    race=data['race'],
                    pend_desc=data['pend_desc'],
                    monster_desc=data['monster_desc'],
                    atk=data['atk'],
                    defense=data['defense'],
                    level=data['level'],
                    attribute=data['attribute'],
                    archetype=data['archetype'],
                    scale=data['scale'],
                    linkval=data['linkval'],
                    linkmarkers=data['linkmarkers'],
                    ygoprodeck_url=data['ygoprodeck_url'],
                    album_card=new_album_card
                )
                
                # Crear instancias de CardSet
                for set_data in data['card_sets']:
                    card_set = CardSet.objects.create(
                        set_name=set_data['set_name'],
                        set_code=set_data['set_code'],
                        set_rarity=set_data['set_rarity'],
                        set_rarity_code=set_data['set_rarity_code'],
                        set_price=set_data['set_price']
                    )
                    card.card_sets.add(card_set)
                
                # Crear instancias de CardImage
                for image_data in data['card_images']:
                    CardImage.objects.create(
                        card=card,
                        image_url=image_data['image_url'],
                        image_url_small=image_data['image_url_small'],
                        image_url_cropped=image_data['image_url_cropped']
                    )
                
                # Crear instancias de CardPrice
                for price_data in data['card_prices']:
                    CardPrice.objects.create(
                        card=card,
                        cardmarket_price=price_data['cardmarket_price'],
                        tcgplayer_price=price_data['tcgplayer_price'],
                        ebay_price=price_data['ebay_price'],
                        amazon_price=price_data['amazon_price'],
                        coolstuffinc_price=price_data['coolstuffinc_price']
                    )
        
        album_cards = AlbumCard.objects.filter(album=user_album, stock__gt=0)
        
        context = {
            'cards': album_cards,
        }
        
        return render(request, 'dashboard/album/index.html', context)
    
    return HttpResponse('<p>Método no permitido</p>', status=405)