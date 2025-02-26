from django.shortcuts import render,get_object_or_404
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


def shop_deck_card(request,pk):
    print(_show_shop_deck_cards(request,pk))
    return render(request, 'shop/deck/detail.html', context=_show_shop_deck_cards(request,pk))


def shop_deck_cards_search_result(request,pk):
    return render(request, 'shop/deck/partials/card_list.html', context=_show_shop_deck_cards(request,pk))


def _show_shop_deck_cards(request,pk):
    deck = get_object_or_404(AlbumDecks,pk=pk)
    cards=deck.deck_cards.all()
    if request.method == 'POST':
        keywords = request.POST.get('keywords', '')
        cards = deck.deck_cards.filter( Q(name__icontains = keywords) | Q(version__icontains = keywords) | Q(konami_id__icontains = keywords) |
                                    Q(archetype__icontains = keywords) | Q(expantion__icontains = keywords)
                                    | Q(type__icontains = keywords)).distinct()
    context={
        "deck":deck,
        "cards":cards
        }    
    return context