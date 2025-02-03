from django.contrib import admin
from apps.card.models import Album, AlbumCard, AlbumDecks,AlbumDecksCard

# Register your models here.

admin.site.register(Album)
admin.site.register(AlbumCard)
admin.site.register(AlbumDecks)
admin.site.register(AlbumDecksCard)