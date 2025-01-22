from django import forms
from apps.card.models import AlbumCard


        
class UpdateAlbumCardForm(forms.ModelForm):
    
    class Meta:
        model = AlbumCard
        fields = ["price","stock","rarity","version","expantion"]