from django import template

register = template.Library()

@register.filter
def deck_in_cart(deck, cart):
    product_id = f"deck{deck.pk}"
    return product_id in cart

@register.filter
def quantity_deck_in_cart(deck, cart):
    product_id = f"deck{deck.pk}"
    return cart[product_id]['cant'] if product_id in cart else 0