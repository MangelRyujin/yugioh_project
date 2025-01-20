from apps.card.models import AlbumCard
import django_filters

class AlbumCardFilter(django_filters.FilterSet):
    name=  django_filters.CharFilter(lookup_expr='icontains')
    konami_id=  django_filters.CharFilter(lookup_expr='icontains')

    rarity = django_filters.ChoiceFilter(choices=AlbumCard.RARITY_CARD)
    version = django_filters.ChoiceFilter(choices=AlbumCard.VERSION_CARD)
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    stock_min = django_filters.NumberFilter(field_name='stock', lookup_expr='gte')
    stock_max = django_filters.NumberFilter(field_name='stock', lookup_expr='lte')
    name = django_filters.CharFilter(lookup_expr='icontains')
    type = django_filters.CharFilter(lookup_expr='icontains')
    attribute = django_filters.CharFilter(lookup_expr='icontains')
    archetype = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = AlbumCard
        fields = ['name','konami_id', 'rarity', 'version', 'price_min', 'price_max', 'stock_min', 'stock_max', 'name', 'type', 'attribute', 'archetype']
        

