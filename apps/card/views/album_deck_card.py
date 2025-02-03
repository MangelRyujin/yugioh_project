from django.shortcuts import render
from apps.card.form import UpdateAlbumDecksCardForm
from apps.card.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
# Create your views here.



@login_required(login_url='/login/')
def album_deck_card_update(request,pk):
    card=get_object_or_404(AlbumDecksCard,deck__user=request.user,pk=pk)
    context={
        'card' : card,
        'form' : UpdateAlbumDecksCardForm(instance=card)
    }
    return render(request, 'dashboard/album/album_card_update/index.html',context)



@login_required(login_url='/login/')
def album_deck_card_form_update(request,pk):
    card=get_object_or_404(AlbumDecksCard,deck__user=request.user,pk=pk)
    form = UpdateAlbumDecksCardForm(instance=card)
    message=''
    if request.POST:
        form = UpdateAlbumDecksCardForm(request.POST,instance=card)
        if form.is_valid():
            form.save()
            message="Carta editada correctamente!!!"
    context={
        'card':card,
        'form':form,
        'message': message
    }
    return render(request, 'components/album/album_card_edit/form.html',context)