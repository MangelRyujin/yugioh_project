from django.shortcuts import render
from apps.card.filters import AlbumDeckFilter
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




@login_required
def album_deck(request):
    return render(request,'dashboard/deck/index.html',_show_decks(request))


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

