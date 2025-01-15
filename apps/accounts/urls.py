from django.urls import path
from apps.accounts.views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('register/', register_view, name='register'),
    path('perfil/', profile_view, name='profile'),
    path('profile/update/', update_profile_view, name='update_profile'),
    path('profile/change-password/', change_password_view, name='change_password'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),
]
