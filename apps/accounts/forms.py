from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from apps.accounts.models import Donation, User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.IntegerField(required=True)
    first_name = forms.CharField()
    last_name = forms.CharField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password1', 'password2','first_name','last_name']

class ProfileUpdateForm(UserChangeForm):
    phone_number = forms.IntegerField(required=False)
    city = forms.CharField(required=False)
    state = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'city', 'state']
        

class CustomPasswordChangeForm(forms.Form):
    new_password1 = forms.CharField(
        label="Nueva contraseña",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text="Tu nueva contraseña debe cumplir con las políticas de seguridad."
    )
    new_password2 = forms.CharField(
        label="Confirmar nueva contraseña",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get("new_password1")
        new_password2 = cleaned_data.get("new_password2")

        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data

    def save(self):
        new_password = self.cleaned_data["new_password1"]
        self.user.set_password(new_password)
        self.user.save()
        
        
class DonationForm(forms.Form):
    
    
    class Meta:
        model = Donation
        fields = ['user', 'amount', 'code', 'message']