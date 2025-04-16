from django.shortcuts import render,get_object_or_404
from apps.card.models import AlbumDecks, AlbumDecksCard
from apps.card.filters import AlbumDeckFilter
from django.db.models import Q
from django.db.models import Count

from apps.shop.cart_instance import Cart
from utils.methods import _get_paginator

def shop_deck(request):
    context=_show_decks(request)
    context['cart'] = Cart(request)
    return render(request, 'shop/deck/index.html',context )

def decks_search_result(request):
    context=_show_decks_filter(request)
    context['cart'] = Cart(request)
    return render(request, 'shop/deck/partials/decks_list.html',context )


def _show_decks(request):
    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()
    decks = AlbumDecks.objects.filter(is_active=True).annotate(total_cards_count=Count('deck_cards')).filter(total_cards_count__gt=0)
    context = _get_paginator(request, decks)
    context['parameters'] = parameters
    return context


def shop_deck_card(request,pk):
    context=_show_shop_deck_cards(request,pk)
    context['deck_in_cart'] = f"deck{context['deck'].pk}" in Cart(request).cart.keys()#Cart(request).cart[f"deck{context['deck'].pk}"]
    return render(request, 'shop/deck/detail.html', context)


def shop_deck_cards_search_result(request,pk):
    return render(request, 'shop/deck/partials/card_list.html', context=_show_shop_deck_cards(request,pk))


def _show_decks_filter(request):
    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()
    decks = AlbumDeckFilter(request.GET, queryset=AlbumDecks.objects.filter(is_active=True).annotate(total_cards_count=Count('deck_cards')).filter(total_cards_count__gt=0))
    context = _get_paginator(request, decks.qs)
    context['parameters'] = parameters
    return context

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


def shop_deck_card_cart_instance_add(request,pk):
    product = AlbumDecks.objects.filter(pk=pk).first()
    cart = Cart(request)
    cart.add_cart('deck',product,1)
    context={
        'deck':product,
        'deck_in_cart': f"deck{product.pk}" in cart.cart.keys()
    }
    return render(request, 'components/cart/index.html', context)

def shop_deck_card_cart_instance_remove(request,pk):
    product = AlbumDecks.objects.filter(pk=pk).first()
    cart = Cart(request)
    cart.remove(product,'deck')
    context={
        'deck':product,
        'deck_in_cart':False
    }
    return render(request, 'components/cart/index.html', context)