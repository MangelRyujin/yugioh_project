from django.urls import path
from apps.forum.views.forum_views import forum_view

urlpatterns = [
    path('', forum_view, name='forum_view'),
]