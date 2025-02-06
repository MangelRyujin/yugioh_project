from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from apps.accounts.decorators import user_is_not_authenticated
from apps.accounts.forms import DonationForm, RegisterForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from apps.accounts.forms import CustomPasswordChangeForm
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from apps.card.models import Album

# Create your views here.

@user_is_not_authenticated
def login_view(request):
    context = {
        "next": request.GET.get('next','')

    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.POST.get('next') or '/'
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(next_url)
        else:
            context['error'] = 'Credenciales incorrectas!'
                    
    return render(request, 'accounts/login.html', context)

@user_is_not_authenticated
def register_view(request):
    form=RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            Album.objects.create(
                user=user,
                name=f"Album {user.username}"
            )
            login(request, user)
            return redirect('/')
            
    return render(request, 'accounts/register.html', {'form': form})

def profile_view(request):
    return render(request, 'accounts/profile/profile.html')


@login_required(login_url='/login/')
def change_password_view(request):
    if request.method == 'POST':
        context = {}
        #form = CustomPasswordChangeForm(request.POST, user=request.user)
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            context['form']=form
            update_session_auth_hash(request, request.user)  # Mantener la sesión iniciada
            messages.success(request, 'Tu contraseña ha sido cambiada exitosamente.')
            return render(request, 'components/dashboard/user/forms/change_password/partials/change_password_form.html', context)
        context['form']=form
        messages.error(request, 'Por favor corrige los errores que se muestran.')
        return render(request, 'components/dashboard/user/forms/change_password/partials/change_password_form.html', context)
    

def update_profile_view(request):
    if request.method == 'POST':
        context = {}
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            context['form']=form
            user.save()
            messages.success(request, 'Tu perfil ha sido actualizado con éxito.')
            if request.headers.get('HX-Request'):
                return render(request, 'components/dashboard/card_user_presentation/partials/user_info.html', context)
            return redirect('profile')
        else:
            messages.error(request, 'Por favor corrige los errores a continuación.')
            if request.headers.get('HX-Request'):
                return render(request, 'components/dashboard/card_user_presentation/partials/user_info.html', context)
        context['form'] = form
        return render(request, 'accounts/profile/profile.html', context)
    
class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('login')
    
    
@login_required(login_url='/login/')
def donation_view(request):
    form= DonationForm()
    if request.method == 'POST':
        form= DonationForm(request.POST)
        if form.is_valid():
            donation=form.save(commit=False)
            donation.user = request.user
            donation.save()
    context={
            "form":form
        }
    return render(request, 'donation/index.html', context)