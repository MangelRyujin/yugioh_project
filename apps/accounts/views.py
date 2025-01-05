from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from apps.accounts.forms import RegisterForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash


# Create your views here.

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


def update_profile_view(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            password1 = form.cleaned_data.get('password1')
            if password1:
                user.set_password(password1)
            user.save()
            if password1:
                update_session_auth_hash(request, user)  # Mantener la sesión iniciada después de cambiar la contraseña
            messages.success(request, 'Tu perfil ha sido actualizado con éxito.')
            return redirect('profile')
        else:
            messages.error(request, 'Por favor corrige los errores a continuación.')
    else:
        form = ProfileUpdateForm(instance=request.user)
    
    return render(request, 'accounts/profile/profile.html', {
        'form': form
    })