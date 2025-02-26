from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.contenttypes.models import ContentType
from cart import Cart, CartItem, AlbumCard, AlbumDecksCard

def add_to_cart(request, content_type_id, object_id):
    content_type = get_object_or_404(ContentType, id=content_type_id)
    content_object = get_object_or_404(content_type.model_class(), id=object_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart.add_item(content_object)
    return redirect('cart_detail')

def remove_from_cart(request, content_type_id, object_id):
    content_type = get_object_or_404(ContentType, id=content_type_id)
    content_object = get_object_or_404(content_type.model_class(), id=object_id)
    cart = get_object_or_404(Cart, user=request.user)
    cart.remove_item(content_object)
    return redirect('cart_detail')

def clear_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart.clear_cart()
    return redirect('cart_detail')

def increase_quantity(request, content_type_id, object_id):
    content_type = get_object_or_404(ContentType, id=content_type_id)
    content_object = get_object_or_404(content_type.model_class(), id=object_id)
    cart = get_object_or_404(Cart, user=request.user)
    cart.increase_quantity(content_object)
    return redirect('cart_detail')

def decrease_quantity(request, content_type_id, object_id):
    content_type = get_object_or_404(ContentType, id=content_type_id)
    content_object = get_object_or_404(content_type.model_class(), id=object_id)
    cart = get_object_or_404(Cart, user=request.user)
    cart.decrease_quantity(content_object)
    return redirect('cart_detail')

def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart/cart_detail.html', {'cart': cart})