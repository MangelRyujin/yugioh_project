from django import forms
from apps.card.models import AlbumCard, AlbumDecksCard,AlbumDecks


        
class UpdateAlbumCardForm(forms.ModelForm):
    
    class Meta:
        model = AlbumCard
        fields = ["price","stock","rarity","version","expantion"]
        
class UpdateAlbumDecksCardForm(forms.ModelForm):
    
    class Meta:
        model = AlbumDecksCard
        fields = ["stock","rarity","version","expantion"]
        
class UpdateAlbumDecksForm(forms.ModelForm):
    
    class Meta:
        model = AlbumDecks
        fields = ["name","description","image","is_active","price"]