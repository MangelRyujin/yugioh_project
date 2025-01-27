from apps.card.models import AlbumCard
import django_filters

class AlbumCardFilter(django_filters.FilterSet):
    konami_id =  django_filters.CharFilter(lookup_expr='icontains')
    name =  django_filters.CharFilter(lookup_expr='icontains')
    rarity = django_filters.CharFilter(method='filter_rarity')
    version = django_filters.CharFilter(method='filter_version')
    atk = django_filters.NumberFilter(field_name='atk', lookup_expr='exact')
    defense = django_filters.NumberFilter(field_name='defense', lookup_expr='exact')
    level = django_filters.NumberFilter(field_name='level', lookup_expr='exact')
    price = django_filters.NumberFilter(field_name='price', method='filter_price')
    type = django_filters.CharFilter(lookup_expr='icontains')
    attribute = django_filters.CharFilter(method='filter_attribute')
    archetype = django_filters.CharFilter(lookup_expr='icontains')

    #RARITY_MAP = dict(AlbumCard.RARITY_CARD)
    RARITY_MAP = {key: value for key, value in AlbumCard.RARITY_CARD}
    VERSION_MAP = {key: value for key, value in AlbumCard.VERSION_CARD}
    ATTRIBUTE_MAP = {key: value for key, value in AlbumCard.ATTRIBUTE_CARD}

    def filter_rarity(self, queryset, name, value):
        mapped_value = self.RARITY_MAP.get(value, None)
        if mapped_value:
            return queryset.filter(rarity=value)
        else:
            return queryset

    def filter_version(self, queryset, name, value):
        mapped_value = self.VERSION_MAP.get(value, None)
        if mapped_value:
            return queryset.filter(version=value)
        else:
            return queryset

    def filter_attribute(self, queryset, name, value):
        mapped_value = self.ATTRIBUTE_MAP.get(value, None)
        if mapped_value:
            return queryset.filter(attribute=value)
        else:
            return queryset

    def filter_price(self, queryset, name, value):
        exact_match = queryset.filter(**{name: value})
        if exact_match.exists():
            return exact_match
        else:
            return queryset.filter(**{f"{name}__gte": value}).order_by(name)

    class Meta:
        model = AlbumCard
        fields = ['konami_id', 'name', 'rarity', 'version', 'atk', 'defense', 'price', 'attribute', 'archetype']