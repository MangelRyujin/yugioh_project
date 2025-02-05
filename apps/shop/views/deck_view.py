from django.shortcuts import render
from apps.card.models import AlbumDecks, AlbumDecksCard
from django.db.models import Q

from utils.methods import _get_paginator

def shop_deck(request):
    return render(request, 'shop/deck/index.html', context=_show_decks(request))

def decks_search_result(request):
    return render(request, 'shop/deck/partials/decks_list.html', context=_show_decks(request))


def _show_decks(request):
    decks = AlbumDecks.objects.filter(is_active=True)
    if request.method == 'POST':
        keywords = request.POST.get('keywords', '')
        decks_search = decks.filter(
            Q(name__icontains = keywords) 
            | Q(user__username__icontains = keywords) 
            | Q(description__icontains = keywords)
            ).distinct()
        decks=decks_search
    return _get_paginator(request,decks)


def shop_card(request):
    return render(request, 'shop/index.html', context=_show_cards(request))


def cards_search_result(request):
    return render(request, 'shop/partials/cards_list.html', context=_show_cards(request))


def _show_cards(request,pk):
    cards = AlbumDecksCard.objects.all()
    if request.method == 'POST':
        keywords = request.POST.get('keywords', '')
        cards_search = cards.filter( Q(name__icontains = keywords) ).distinct()
        cards=cards_search
    return _get_paginator(request,cards)