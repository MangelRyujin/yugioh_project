from django.contrib import admin
from apps.card.models import Album, AlbumCard

# Register your models here.

admin.site.register(Album)
admin.site.register(AlbumCard)