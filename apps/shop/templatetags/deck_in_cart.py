from django import template

register = template.Library()

@register.filter
def deck_in_cart(album_deck, cart):
    if f"deck{album_deck.pk}" in cart.cart.keys():
        return True
    return False


@register.filter
def quantity_deck_in_cart(album_deck, cart):
    product_id = f"deck{album_deck.pk}"
    return cart[product_id]['cant'] if product_id in cart else 0