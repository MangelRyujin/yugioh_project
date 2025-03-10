from apps.card.models import AlbumCard
from apps.shop.cart_instance import Cart
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.http import HttpResponse


def cart_view(request):
    cart= Cart(request)
    element_last = cart.last_element()
    context = {
        'cart':cart.cart.values(),
        'element_last': element_last
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

def increment_cart_item(request, pk, object):
    cart = Cart(request)
    if object == 'card':
        album_card = AlbumCard.objects.filter(pk=pk).first()
        cart.increment(album_card,object)
        return render(request, 'components/cart/card/card.html', {'item': cart.cart[f'{object}{pk}']})
    return render(request, 'components/cart/card/card.html', {'error': 'Item not found'})

def decrement_cart_item(request, pk, object):
    cart = Cart(request)
    if object == 'card':
        album_card = AlbumCard.objects.filter(pk=pk).first()
        cart.decrement(album_card, object)
        element_last = cart.last_element()
        context = {
            'cart': cart.cart.values(),
            'element_last': element_last
        }
        return render(request, 'components/cart/cart_list.html', context)
    return HttpResponse('')

def remove_cart_item(request, pk, object):
    cart = Cart(request)
    if object == 'card':
        album_card = AlbumCard.objects.filter(pk=pk).first()
        cart.remove(album_card, object)
        element_last = cart.last_element()
        context = {
            'cart': cart.cart.values(),
            'element_last': element_last
        }
        return render(request, 'components/cart/cart_list.html', context)
    return HttpResponse('')
        
    
def clear_cart_instance(request):
    cart = Cart(request)
    cart.clear_items()
    context={
        'cart':[]
    }
    return render(request, 'components/cart/cart_list.html',context)