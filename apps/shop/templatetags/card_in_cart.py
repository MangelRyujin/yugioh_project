from django import template


register = template.Library()


# @register.simple_tag
@register.filter('card_in_cart')
def card_in_cart(album_card,cart):
    if f"card{album_card.pk}" in cart.cart.keys():
        return True
    return False

# @register.simple_tag
@register.filter('quantity_card_in_cart')
def quantity_card_in_cart(album_card,cart):
    card=cart.cart[f"card{album_card.pk}"]
    if card:
        if card['cant'] > 99:
            return f"99+"
        return card['cant']
    return 0