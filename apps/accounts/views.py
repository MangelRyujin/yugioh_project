from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from apps.accounts.forms import RegisterForm

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
        else:
            print("no")
    return render(request, 'accounts/register.html', {'form': form})
