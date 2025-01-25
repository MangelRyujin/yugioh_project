import json
from django.shortcuts import render
from apps.card.models import AlbumCard
from apps.card.filters import AlbumCardFilter
from django.contrib.auth.decorators import login_required

@login_required
def shop_view(request):
    
    return render(request, 'shop/index.html')

import json
from django.shortcuts import render
from apps.card.models import AlbumCard
from django.contrib.auth.decorators import login_required

@login_required
def search_cards(request):
    if request.method == 'POST':
        keyword = request.POST.get('kbdInput4')
        filters = {key: value for key, value in request.POST.items() if value and key not in ['kbdInput4', 'csrfmiddlewaretoken', 'filters']}
        
        # Obtener filtros del contexto si existen
        context_filters = request.POST.get('filters', '{}')
        
        # Verificar si context_filters está vacío
        if context_filters:
            # imprime los filtros pasados por contexto
            try:
                # Asegurarse de que context_filters esté en formato JSON válido
                if isinstance(context_filters, str):
                    context_filters = json.loads(context_filters.encode().decode('unicode_escape').replace("'", '"'))
                    print("Filtros pasados por contexto decodificados:", context_filters)
                else:
                    context_filters = {}
            except json.JSONDecodeError as e:
                # Manejar el error de decodificación JSON
                print(f"Error decodificando JSON: {e}")
                print(f"Contenido de context_filters: {context_filters}")
                context_filters = {}
        else:
            context_filters = {}
        
        # Combinar filtros del formulario y del contexto
        combined_filters = {**context_filters, **filters}
        
        if combined_filters:
            album_cards = AlbumCard.objects.select_related('album__user').filter(name__icontains=keyword, **combined_filters)
            print("YES")
        else:
            print("NO")
            album_cards = AlbumCard.objects.select_related('album__user').filter(name__icontains=keyword)
        
        return render(request, 'shop/partials/cards-list.html', {'album_cards': album_cards, 'filters': combined_filters})

@login_required
def apply_filters(request):
    if request.method == 'POST':
        filters = {key: value for key, value in request.POST.items() if value and key != 'csrfmiddlewaretoken'}
        return render(request, 'shop/index.html', {'filters': filters})

@login_required
def search_cards_filter(request):
    album_cards = AlbumCard.objects.select_related('album__user').all()
    album_card_filter = AlbumCardFilter(request.GET, queryset=album_cards)
    return render(request, 'shop/partials/cards-list.html', {'filter': album_card_filter})