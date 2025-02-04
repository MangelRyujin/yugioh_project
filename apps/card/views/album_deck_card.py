from django.shortcuts import render
from apps.card.form import UpdateAlbumDecksCardForm
from apps.card.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
import requests
from django.http import  HttpResponse
from apps.card.utils.create_card import album_deck_card_create
# Create your views here.


@login_required(login_url='/login/')
def search_deck_user_cards(request,pk):
    deck = get_object_or_404(AlbumDecks,pk = pk)
    context={
        "deck":deck,
        "cards": deck.deck_cards.all().order_by('name')
    }  
    return render(request, 'components/deck/detail/card/card_list.html',context)



@login_required(login_url='/login/')
def search_deck_cards_modal(request):
    deck_id=request.GET.get('deck_id','')
    if request.method == 'POST':
        query = request.POST['keywordDeckCardAdd'] or ''
        external_api_url = f'https://primervirgen.pythonanywhere.com/api/cards/?name={query}'
        try:
            response = requests.get(external_api_url)
            if response.status_code == 200:
                data = response.json()
                context={
                    'cards': data['results'],
                    'deck_id': deck_id
                }
                return render(request, 'components/deck/detail/card/add_card_modal/search_results.html', context)
            else:
                return HttpResponse('<p>No se encontraron resultados</p>', status=response.status_code)
        except requests.exceptions.RequestException as e:
            return HttpResponse(f'<p>Error: {str(e)}</p>', status=500)
    return HttpResponse('<p>Método no permitido</p>', status=405)



@login_required(login_url='/login/')
def add_deck_card(request,pk):
    deck_id=request.GET.get('deck_id','')
    if request.method == 'POST':
        external_api_url = f'https://primervirgen.pythonanywhere.com/api/cards/?konami_id={pk}' 
        context={}    
        # response para almacenar los datos de la carta
        response = requests.get(external_api_url)
        if response.status_code == 200:
            data = response.json()['results'][0]
            # user_album_card = get_object_or_404(AlbumCard, konami_id=pk)
            cards= album_deck_card_create(request,data,deck_id)
            context['card']=data
            context['deck_id']=deck_id
            context['cards']=cards
            context['message']='Carta añadida correctamente'
            
        return render(request,'components/deck/detail/card/add_card_modal/card_form_add.html',context)

@login_required(login_url='/login/')
def album_deck_card_update(request,pk):
    card=get_object_or_404(AlbumDecksCard,deck__user=request.user,pk=pk)
    context={
        'card' : card,
        'deck_id':request.GET.get('deck_id',''),
        'form' : UpdateAlbumDecksCardForm(instance=card)
    }
    return render(request, 'dashboard/deck/detail/album_deck_card_update/index.html',context)



@login_required(login_url='/login/')
def album_deck_card_form_update(request,pk):
    card=get_object_or_404(AlbumDecksCard,deck__user=request.user,pk=pk)
    form = UpdateAlbumDecksCardForm(instance=card)
    message=''
    if request.POST:
        form = UpdateAlbumDecksCardForm(request.POST,instance=card)
        if form.is_valid():
            form.save()
            message="Carta editada correctamente!!!"
    context={
        'card':card,
        'form':form,
        'message': message
    }
    return render(request, 'components/deck/detail/album_card_edit/form.html',context)


@login_required(login_url='/login/')
def album_deck_card_delete(request,pk):
    card = AlbumDecksCard.objects.get(deck__user=request.user,pk=pk)
    context={
        'card':card
    }
    if request.method == 'DELETE':
        if card:
            card.delete()
            context['card']=[]
            context['message']="Carta eliminada correctamente"
    
    return render(request,'components/album/card.html',context)