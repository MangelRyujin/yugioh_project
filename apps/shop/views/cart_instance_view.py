from apps.card.models import AlbumCard, AlbumDecks
from apps.shop.cart_instance import Cart
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.contrib import messages


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

# def increment_cart_item(request, pk, object):
#     cart = Cart(request)
#     if object == 'card':
#         album_card = AlbumCard.objects.filter(pk=pk).first()
#         cart.increment(album_card, object)
#         return render(request, 'components/cart/card/card.html', {'item': cart.cart[f'{object}{pk}']})
#     elif object == 'deck':
#         album_deck = AlbumDecks.objects.filter(pk=pk).first()
#         cart.increment(album_deck, object)
#         return render(request, 'components/cart/deck/deck.html', {'item': cart.cart[f'{object}{pk}']})
#     return render(request, 'components/cart/card/card.html', {'error': 'Item not found'})

# def increment_cart_item(request, pk, object):
#     cart = Cart(request)
#     if object == 'card':
#         album_card = AlbumCard.objects.filter(pk=pk).first()
#         if album_card:
#             if cart.increment(album_card, object):
#                 return render(request, 'components/cart/card/card.html', {'item': cart.cart[f'{object}{pk}']})
#             else:
#                 messages.error(request, 'Por favor corrige los errores que se muestran.')
#                 print('MauroXXX')
#                 return JsonResponse({'error': 'No hay suficiente stock'}, status=400)
#         else:
#             print('Mauro')
#             return JsonResponse({'error': 'Item not found'}, status=404)
#     elif object == 'deck':
#         album_deck = AlbumDecks.objects.filter(pk=pk).first()
#         if album_deck:
#             if cart.increment(album_deck, object):
#                 return render(request, 'components/cart/deck/deck.html', {'item': cart.cart[f'{object}{pk}']})
#             else:
#                 return JsonResponse({'error': 'No hay suficiente stock'}, status=400)
#         else:
#             return JsonResponse({'error': 'Item not found'}, status=404)
#     return JsonResponse({'error': 'Invalid object type'}, status=400)


def increment_cart_item(request, pk, object):
    cart = Cart(request)
    if object == 'card':
        album_card = AlbumCard.objects.filter(pk=pk).first()
        if album_card:
            if cart.increment(album_card, object):
                return render(request, 'components/cart/card/card.html', {'item': cart.cart[f'{object}{pk}']})
            else:
                messages.error(request, 'No hay suficiente stock')
                return render(request, 'components/cart/card/card.html', {'item': cart.cart[f'{object}{pk}']})
        else:
            messages.error(request, 'Item not found')
            return render(request, 'components/cart/card/card.html', {'error': 'Item not found'})
    elif object == 'deck':
        album_deck = AlbumDecks.objects.filter(pk=pk).first()
        if album_deck:
            if cart.increment(album_deck, object):
                return render(request, 'components/cart/deck/deck.html', {'item': cart.cart[f'{object}{pk}']})
            else:
                messages.error(request, 'No hay suficiente stock')
                return render(request, 'components/cart/deck/deck.html', {'item': cart.cart[f'{object}{pk}']})
        else:
            messages.error(request, 'Item not found')
            return render(request, 'components/cart/deck/deck.html', {'error': 'Item not found'})
    messages.error(request, 'Invalid object type')
    return render(request, 'components/cart/card/card.html', {'error': 'Invalid object type'})


def decrement_cart_item(request, pk, object):
    cart = Cart(request)
    if object == 'card':
        album_card = AlbumCard.objects.filter(pk=pk).first()
        cart.decrement(album_card, object)
    elif object == 'deck':
        album_deck = AlbumDecks.objects.filter(pk=pk).first()
        cart.decrement(album_deck, object)
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


from django.http import JsonResponse

def check_stock(request, pk, object):
    cart = Cart(request)
    if object == 'card':
        product = AlbumCard.objects.filter(pk=pk).first()
    elif object == 'deck':
        product = AlbumDecks.objects.filter(pk=pk).first()
    else:
        return JsonResponse({'error': 'Invalid object type'}, status=400)

    if not product:
        return JsonResponse({'error': 'Product not found'}, status=404)

    product_id = f"{object}{product.pk}"
    if product_id in cart.cart:
        desired_quantity = cart.cart[product_id]['cant']
        if desired_quantity > product.stock:
            return JsonResponse({'in_stock': False}, status=200)
        else:
            return JsonResponse({'in_stock': True}, status=200)
    else:
        return JsonResponse({'error': 'Product not in cart'}, status=404)