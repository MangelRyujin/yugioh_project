from django.shortcuts import render
from apps.card.filters import AlbumDeckFilter
from apps.card.form import UpdateAlbumDecksForm
from apps.card.models import *
import requests
from django.http import  HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.card.models import AlbumCard, Album
import requests
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from apps.card.utils.create_card import album_card_create
from django.db.models import Q
# Create your views here.




@login_required(login_url='/login/')
def album_deck(request):
    return render(request,'dashboard/deck/index.html',_show_decks(request))

@login_required(login_url='/login/')
def search_album_deck(request):
    return render(request,'components/deck/deck_list.html',_show_decks(request))

@login_required(login_url='/login/')
def _show_decks(request):
    keyword = request.GET.get('kbdInput2','')
    if request.method == 'POST':
        keyword = request.POST.get("kbdInput2",'')
    search_card = AlbumDecks.objects.filter(name__icontains=keyword,user=request.user).order_by('name')
    cards = AlbumDeckFilter(request.GET, queryset=search_card)
    paginator = Paginator(cards.qs, 25)    # Show 25 contacts per page.
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    context={
        'pagination':page_obj,
        'kbdInput2':keyword
    }
    return context


@login_required(login_url='/login/')
def create_album_deck(request):
    AlbumDecks.objects.create(
        user=request.user,
        name=f"Nuevo deck",
        description="Descripción"
        )
    context=_show_decks(request)
    context['create_message']="Deck creado con éxito"
    return render(request,'components/deck/deck_list.html',context)


@login_required(login_url='/login/')
def delete_album_deck(request,pk):
    deck = get_object_or_404(AlbumDecks,pk = pk)
    context={
        "deck":deck,
        
    }
    if request.method == 'DELETE':
        if deck:
            deck.delete()
            context['deck']=[]
            context['message']="Deck eliminado con éxito"
    return render(request,'components/deck/deck.html',context)


@login_required(login_url='/login/')
def album_deck_detail(request,pk):
    deck = get_object_or_404(AlbumDecks,pk = pk)
    context={
        "deck":deck,
        "cards": deck.deck_cards.all().order_by('name'),
        "form": UpdateAlbumDecksForm(instance=deck)
    }
    return render(request,'dashboard/deck/detail/index.html',context)

@login_required(login_url='/login/')
def update_deck_profile(request,pk):
    deck = get_object_or_404(AlbumDecks,pk = pk)
    form=UpdateAlbumDecksForm(instance=deck)
    context={
        "deck":deck,
    }
    if request.POST:
        
        form=UpdateAlbumDecksForm(request.POST,request.FILES,instance=deck)
        if form.is_valid():
            form.save()
            context['message']="Deck editado con éxito"
            context['form']=form
        else:
            pass
    return render(request,'components/deck/detail/deck/deck_perfil.html',context)