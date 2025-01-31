from django import forms
from apps.card.models import AlbumCard

class CustomDecimalField(forms.DecimalField):
    def to_python(self, value):
        return super().to_python(value.replace(',', '.'))
        
class UpdateAlbumCardForm(forms.ModelForm):
    price = CustomDecimalField(
        max_digits=10,
        decimal_places=2,
        required=True,
        min_value=0.01
    )
    class Meta:
        model = AlbumCard
        fields = ["price","stock","rarity","version","expantion"]