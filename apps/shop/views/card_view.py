from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from apps.card.models import AlbumCard
from apps.card.filters import AlbumCardFilter
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from utils.methods import _get_paginator

def shop(request):
    return render(request, 'shop/shop.html')

def shop_card(request):
    content_type = ContentType.objects.get_for_model(AlbumCard)
    context = _show_cards(request)
    context['content_type_id'] = content_type.id
    return render(request, 'shop/index.html', context)

def cards_search_result(request):
    return render(request, 'shop/partials/cards_list.html', context=_show_cards(request))

def cards_filter_result(request):
    context = _show_cards_filter(request)
    content_type = ContentType.objects.get_for_model(AlbumCard)
    context['content_type_id'] = content_type.id
    return render(request, 'shop/partials/cards_list.html', context)

def _show_cards_filter(request):
    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()
    cards = AlbumCardFilter(request.GET, queryset=AlbumCard.objects.all().order_by('id'))
    context = _get_paginator(request, cards.qs)
    context['parameters'] = parameters
    return context

def _show_cards(request):
    cards = AlbumCard.objects.all().order_by('id')
    context = _get_paginator(request, cards)
    return context