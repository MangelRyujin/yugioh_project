from django.shortcuts import render
from apps.card.filters import AlbumCardFilter
from apps.card.models import *
from django.http import  HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.card.models import AlbumCard, Album
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from apps.card.utils.create_card import album_card_create
from django.db.models import Q
import requests
# Create your views here.



@login_required(login_url='/login/')
def search_user_cards(request):
    context=_show_cards(request)
    context['search']=True
    return render(request, 'components/album/card_list.html',context)


@login_required(login_url='/login/')
def search_cards_modal(request):
    if request.method == 'POST':
        
        query = request.POST['kbdInput1'] or ''
        external_api_url = f'https://primervirgen.pythonanywhere.com/api/cards/?name={query}'
        try:
            response = requests.get(external_api_url)
            if response.status_code == 200:
                data = response.json()
               
                return render(request, 'components/album/add_card_modal/search_results.html', {'cards': data['results']})
            else:
                return HttpResponse('<p>No se encontraron resultados</p>', status=response.status_code)
        except requests.exceptions.RequestException as e:
            return HttpResponse(f'<p>Error: {str(e)}</p>', status=500)
    return HttpResponse('<p>Método no permitido</p>', status=405)

@login_required
def album(request):
    return render(request,'dashboard/album/index.html',_show_cards(request))


@login_required(login_url='/login/')
def add_card(request,pk):
    if request.method == 'POST':
        external_api_url = f'https://primervirgen.pythonanywhere.com/api/cards/?konami_id={pk}' 
        context={}    
        response = requests.get(external_api_url)
        if response.status_code == 200:
            data = response.json()['results'][0]
            cards= album_card_create(request,data)
            context['card']=data
            context['cards']=cards
            context['message']='Carta añadida correctamente'
            
        return render(request,'components/album/add_card_modal/card_form_add.html',context)
    

@login_required(login_url='/login/')
def _show_cards(request):
    keyword = request.GET.get('kbdInput2','')
    if request.method == 'POST':
        keyword = request.POST.get("kbdInput2",'')
    search_card = AlbumCard.objects.filter(name__icontains=keyword,album__user=request.user).order_by('-id')
    cards = AlbumCardFilter(request.GET, queryset=search_card)
    paginator = Paginator(cards.qs, 60)    # Show 40 contacts per page.
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    context={
        'pagination':page_obj,
        'kbdInput2':keyword
    }
    return context


@login_required(login_url='/login/')
def album_card_delete(request,pk):
    card = AlbumCard.objects.get(album__user=request.user,pk=pk)
    context={
        'card':card
    }
    if request.method == 'DELETE':
        if card:
            card.delete()
            context['card']=[]
            context['message']="Carta eliminada correctamente"
    
    return render(request,'components/album/card.html',context)