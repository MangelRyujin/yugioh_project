from django import forms
from apps.card.models import AlbumCard, AlbumDecksCard


        
class UpdateAlbumCardForm(forms.ModelForm):
    
    class Meta:
        model = AlbumCard
        fields = ["price","stock","rarity","version","expantion"]
        
class UpdateAlbumDecksCardForm(forms.ModelForm):
    
    class Meta:
        model = AlbumDecksCard
        fields = ["stock","rarity","version","expantion"]