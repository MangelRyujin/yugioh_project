from apps.card.models import AlbumCard, AlbumDecks
from apps.shop.cart_instance import Cart
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse


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
    product = []
    cart=Cart(request)
    context = {
       
    }
    if object == 'card':
        product = AlbumCard.objects.filter(pk=pk).first()
        context['album_card']=product
        template='shop/partials/card.html'
    elif object == 'deck':
        product = AlbumDecks.objects.filter(pk=pk).first()
        context['album_deck']=product
        template='shop/deck/partials/deck.html'
    cart.add_cart(object,product,1)
    context['cart']=cart
    return render(request, template ,context)


def remove_to_cart_instance(request, pk, object):
    product = []
    cart=Cart(request)
    context={}
    if object == 'card':
        product = AlbumCard.objects.filter(pk=pk).first()
        context['album_card']=product
        template='shop/partials/card.html'
    elif object == 'deck':
        product = AlbumDecks.objects.filter(pk=pk).first()
        context['album_deck']=product
        template='shop/deck/partials/deck.html'
    cart.remove(product,object)
    context['cart'] = cart
    return render(request, template,context)

def increment_cart_item(request, pk, object):
    cart = Cart(request)
    if object == 'card':
        album_card = AlbumCard.objects.filter(pk=pk).first()
        if album_card:
            if cart.increment(album_card, object):
                return render(request, 'components/cart/card/card.html', {'item': cart.cart[f'{object}{pk}']})
            else:
                messages.error(request, 'No hay suficiente cantidad en stock')
                return render(request, 'components/cart/card/card.html', {'item': cart.cart[f'{object}{pk}']})
        else:
            messages.error(request, 'Item not found')
            return render(request, 'components/cart/card/card.html', {'error': 'Item not found'})
    messages.error(request, 'Invalid object type')
    return render(request, 'components/cart/card/card.html', {'error': 'Invalid object type'})


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


def remove_cart_item(request, pk, object):
    cart = Cart(request)
    if object == 'card':
        product = AlbumCard.objects.filter(pk=pk).first()
        cart.remove(product, object)
    elif object == 'deck':
        product = AlbumDecks.objects.filter(pk=pk).first()
        cart.remove(product, object)
    element_last = cart.last_element()
    context = {
        'cart': cart.cart.values(),
        'element_last': element_last
    }
    return render(request, 'components/cart/cart_list.html', context)
    
def clear_cart_instance(request):
    cart = Cart(request)
    cart.clear_items()
    context={
        'cart':[]
    }
    
    return render(request, 'components/cart/cart_list.html',context)

def check_cart(request):
    cart = Cart(request)
    quantityAdjusting = False
    adjusted_items = []
    zero_quantity_items = []
    text = 'text'
    cart_validated = False
    message = {
        'tag': '',
        'header': '',
        'text': '',
    }
    for item in list(cart.cart.values()):
        if item['object'] == 'card':
            product = AlbumCard.objects.filter(pk=item['pk']).first()
        elif item['object'] == 'deck':
            product = AlbumDecks.objects.filter(pk=item['pk']).first()
        else:
            continue

        if item['object'] == 'card' and item['cant'] > product.stock:
            quantityAdjusting = True
            item['cant'] = product.stock
            if item['cant'] == 0:
                zero_quantity_items.append(item['pk'])
            else:
                cart.cart[f"{item['object']}{item['pk']}"]['cant'] = product.stock
                cart.save()
                adjusted_items.append(item['pk'])
            
        if item['object'] == 'card' and item['cant'] == 0:
            zero_quantity_items.append(item['pk'])

        if item['object'] == 'deck' and item['cant'] > product.stock:
            quantityAdjusting = True
            item['cant'] = product.stock
            if item['cant'] == 0:
                zero_quantity_items.append(item['pk'])
            else:
                cart.cart[f"{item['object']}{item['pk']}"]['cant'] = product.stock
                cart.save()
                adjusted_items.append(item['pk'])
        
        if item['object'] == 'deck' and item['cant'] == 0:
            zero_quantity_items.append(item['pk'])
            
    if quantityAdjusting:
        text = 'Cantidad de productos reajustada por ausencia de stock!'    
        message = {
            'tag': 'info',
            'header': 'Información',
            'text': text,
        }
    else:
        message = {
            'tag': 'success',
            'header': 'Confirmación',
            'text': 'Carrito validado correctamente!',
        }
        cart_validated = True

    context = {
        'cart': cart.cart.values(),
        'message': message,
        'adjusted_items': adjusted_items,
        'zero_quantity_items': zero_quantity_items,
        'cart_validated': cart_validated,
    }
    
    if cart_validated:
        return HttpResponseRedirect(reverse('clear_cart_instance'))
    
    return render(request, 'components/cart/cart_list.html', context)