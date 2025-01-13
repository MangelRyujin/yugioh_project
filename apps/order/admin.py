from django.contrib import admin

from apps.order.models import *

# Register your models here.

# admin.site.register(Order)

# @admin.register(Item)
# class ItemAdmin(admin.ModelAdmin):
#     list_display = ['id', 'customer', 'seller','create_date_at', 'create_time_at','price','cant']
#     list_per_page = 100
    

class ItemInline(admin.TabularInline):
    model = Item
    extra = 0
    

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'create_user', 'current_user','current_destination', 'delivery']
    list_per_page = 100
    inlines = [ItemInline]