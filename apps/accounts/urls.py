from django.urls import path
from apps.accounts.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('register/', register_view, name='register'),
    path('perfil/', profile_view, name='profile'),
    path('profile/update/', update_profile_view, name='update_profile'),
    path('profile/change-password/', change_password_form, name='change_password')
]
