from django.contrib import admin
from .models import *
from solo.admin import SingletonModelAdmin
# Register your models here.


admin.site.register(Coin, SingletonModelAdmin)

class FeatureSubscriptionInline(admin.TabularInline):
    model = FeatureSubscription
    extra = 0
    fields = ('subscription',)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'month_price','month_price_CUP', 'annual_price_discount','discount_anual_price','discount_anual_price_cup']
    list_per_page = 100
    readonly_fields=['month_price_CUP','discount_anual_price','discount_anual_price_cup']
    inlines = [FeatureSubscriptionInline]