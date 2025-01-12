from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from apps.accounts.decorators import user_is_not_authenticated
from apps.accounts.forms import RegisterForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from apps.accounts.forms import CustomPasswordChangeForm
from django.http import HttpResponse, JsonResponse

# Create your views here.

@user_is_not_authenticated
def login_view(request):
    context = {
        "next": request.GET.get('next') or '/'
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
        context = {
        'form': form
        }
        return render(request, 'accounts/profile/profile.html', context)