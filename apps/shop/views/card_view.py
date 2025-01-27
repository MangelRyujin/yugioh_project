import json
from django.shortcuts import render
from apps.card.models import AlbumCard
from apps.card.filters import AlbumCardFilter
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from utils.methods import _get_paginator



@login_required
def shop(request):
    return render(request, 'shop/index.html')

@login_required
def shop_card(request):
    return render(request, 'shop/index.html', context=_show_cards(request))

@login_required
def cards_search_result(request):
    return render(request, 'shop/partials/cards_list.html', context=_show_cards(request))

@login_required
def cards_filter_result(request):
    return render(request, 'shop/partials/cards_list.html', context=_show_cards_filter(request))


def _show_cards_filter(request):
    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()
    cards = AlbumCardFilter(request.GET, queryset=AlbumCard.objects.all())
    context=_get_paginator(request,cards.qs)
    context['parameters']=parameters
    return context

def _show_cards(request):
    cards = AlbumCard.objects.all()
    if request.method == 'POST':
        keywords = request.POST.get('keywords', '')
        cards_search = cards.filter( Q(name__icontains = keywords) | Q(type__icontains = keywords)).distinct()
        cards=cards_search
    return _get_paginator(request,cards)
