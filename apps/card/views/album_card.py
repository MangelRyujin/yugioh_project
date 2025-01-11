from django.shortcuts import render
from apps.card.form import UpdateAlbumCardForm
from apps.card.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
# Create your views here.


@login_required
def album_card_update(request,pk):
    card=get_object_or_404(AlbumCard,album__user=request.user,pk=pk)
    context={
        'card' : card,
        'form' : UpdateAlbumCardForm(instance=card)
    }
    return render(request, 'dashboard/album/album_card_update/index.html',context)


@login_required
def album_card_form_update(request,pk):
    card=get_object_or_404(AlbumCard,album__user=request.user,pk=pk)
    form = UpdateAlbumCardForm(instance=card)
    message=''
    if request.POST:
        form = UpdateAlbumCardForm(request.POST,instance=card)
        if form.is_valid():
            form.save()
            message="Carta editada correctamente!!!"
    context={
        'card':card,
        'form':form,
        'message': message
    }
    return render(request, 'components/album/album_card_edit/form.html',context)