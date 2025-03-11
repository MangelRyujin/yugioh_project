from django.shortcuts import render
from apps.card.form import UpdateAlbumCardForm
from apps.card.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
# Create your views here.



@login_required(login_url='/login/')
def forum_view(request):
    return render(request, 'forum/index.html')
