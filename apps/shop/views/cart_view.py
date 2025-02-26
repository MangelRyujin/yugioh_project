import json
from django.shortcuts import render


def cart_view(request):
    return render(request, 'shop/cart.html')