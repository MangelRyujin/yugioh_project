from django.http import JsonResponse, HttpResponse
import requests
from django.shortcuts import render, get_object_or_404
from apps.card.models import *

def create_card(request,pk):
    if request.method == 'POST':
            konami_id = request.POST.get('konami_id', '')
            
            if not konami_id:
                return JsonResponse({'error': 'konami_id es requerido'}, status=400)
            
            # enlace de la peticion
            external_api_url = f'https://primervirgen.pythonanywhere.com/api/cards/?konami_id={pk}'
            
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
                    card = AlbumCard.objects.create(
                        price=request.POST.get('price', 0),
                        rarity = request.POST.get('price', 0),
                        stock = request.POST.get('price', 1),
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
                    
                    
                    
                    # Crear instancias de CardImage
                    for image_data in data['card_images']:
                        CardImage.objects.create(
                            card=card,
                            image_url=image_data['image_url'],
                            image_url_small=image_data['image_url_small'],
                            image_url_cropped=image_data['image_url_cropped']
                        )
            context = {
                'cards': AlbumCard.objects.filter(album=user_album),
            }
            
            return render(request, 'dashboard/album/index.html', context)
        
    return HttpResponse('<p>Método no permitido</p>', status=405)

def album_card_create(request,data):
    album = Album.objects.get(user=request.user)
    card = AlbumCard.objects.create(
                        price=request.POST.get('price', 0),
                        rarity = request.POST.get('rarity', '1'),
                        stock = request.POST.get('stock', 1),
                        version = request.POST.get('version', '1'),
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
                        album=album,
                    )
                    
                    
                    # Crear instancias de CardImage
    for image_data in data['card_images']:
                        CardImage.objects.create(
                            card=card,
                            image_url=image_data['image_url'],
                            image_url_small=image_data['image_url_small'],
                            image_url_cropped=image_data['image_url_cropped']
                        )
    return AlbumCard.objects.filter(album=album)