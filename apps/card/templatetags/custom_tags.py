from django.conf import settings
from django.urls import reverse
from django import template

from apps.card.models import AlbumCard

register = template.Library()


# @register.simple_tag
@register.filter('card_exist')
def card_exist(user,konami_id):
    return AlbumCard.objects.filter(album__user=user, konami_id=konami_id).exists()