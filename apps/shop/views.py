from django.shortcuts import render
from apps.card.models import AlbumCard
from apps.card.filters import AlbumCardFilter
from django.contrib.auth.decorators import login_required

@login_required
def shop_view(request):
    return render(request, 'shop/index.html')

@login_required
def search_cards(request):
    # Obtener todas las AlbumCards de los álbumes asociados a cada usuario
    if request.method == 'POST':
        keyword = request.POST.get('kbdInput4')
    album_cards = AlbumCard.objects.select_related('album__user').filter(name__icontains=keyword)
    return render(request, 'shop/partials/cards-list.html', {'album_cards': album_cards})

@login_required
def search_cards_filter(request):
    album_cards = AlbumCard.objects.select_related('album__user').all()
    album_card_filter = AlbumCardFilter(request.GET, queryset=album_cards)
    return render(request, 'shop/partials/cards-list.html', {'filter': album_card_filter})
