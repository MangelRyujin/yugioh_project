from apps.card.models import AlbumCard
import django_filters

class AlbumCardFilter(django_filters.FilterSet):
    name=  django_filters.CharFilter(lookup_expr='icontains')
    konami_id=  django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = AlbumCard
        fields = ['name','konami_id']