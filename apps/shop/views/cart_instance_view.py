from apps.card.models import AlbumCard
from apps.shop.cart_instance import Cart
from django.shortcuts import render, redirect


def cart_view(request):
    cart= Cart(request)
    context = {
        'cart':cart.cart.values()
    }
    return render(request, 'shop/cart.html', context)

def album_card_detail_shop_card(request,pk):
    cart=Cart(request)
    context = {
        'cart':cart,
        'album_card': AlbumCard.objects.filter(pk=pk).first()
    }
    return render(request, 'shop/partials/card.html',context)

def add_to_cart_instance(request, pk, object):
    album_card = []
    cart=Cart(request)
    if object == 'card':
        album_card = AlbumCard.objects.filter(pk=pk).first()
    cart.add_cart(object,album_card,1)
    
    context = {
        'cart':cart,
        'album_card': album_card
    }
    return render(request, 'shop/partials/card.html',context)


def remove_to_cart_instance(request, pk, object):
    album_card = []
    cart=Cart(request)
    if object == 'card':
        album_card = AlbumCard.objects.filter(pk=pk).first()
    cart.remove(album_card,object)
    
    context = {
        'cart':cart,
        'album_card': album_card
    }
    return render(request, 'shop/partials/card.html',context)

from django.http import JsonResponse

def increment_cart_item(request, pk, object):
    cart = Cart(request)
    if object == 'card':
        album_card = AlbumCard.objects.filter(pk=pk).first()
        cart.increment(album_card)
        return JsonResponse({'success': True, 'new_quantity': cart.cart[f'{object}{pk}']['cant']})
    return JsonResponse({'success': False})

def decrement_cart_item(request, pk, object):
    cart = Cart(request)
    if object == 'card':
        album_card = AlbumCard.objects.filter(pk=pk).first()
        cart.decrement(album_card)
        return JsonResponse({'success': True, 'new_quantity': cart.cart[f'{object}{pk}']['cant']})
    return JsonResponse({'success': False})

def remove_cart_item(request, pk, object):
    cart = Cart(request)
    if object == 'card':
        album_card = AlbumCard.objects.filter(pk=pk).first()
        cart.remove(album_card, object)
        return JsonResponse({'success': True, 'new_quantity': 0})
    return JsonResponse({'success': False})
