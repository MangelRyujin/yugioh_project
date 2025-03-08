from decimal import Decimal
from django.conf import settings 
from django.contrib import messages
from django.shortcuts import redirect


class Cart:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        cart=self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID]={}
        self.cart=cart
    
    
    def add_cart(self,object,product,cant):
        product_id = f"{object}{str(product.id)}"
        if cant<1:
            self.remove(product,object)
        else:
            if object == 'card':
                if product_id not in self.cart.keys():
                    self.cart[product_id] = {
                        'pk':product.pk,
                        'object':object,
                        'cant':cant or 0,
                        'price': product.price,
                        'product_name': product.name,
                        'product_rarity':product.get_rarity,
                        'product_version':product.get_version,
                        'product_expantion':product.expantion,
                        'product_type': product.type,
                        'product_image': product.card_images.image_url_small,
                        }
                else:
                    self.cart[product_id]['cant'] = cant
                    self.cart[product_id]['price'] = product.price * cant
            elif object == 'deck':
                pass # Decks proccess
        self.save()
        return True
    
   
    def increment(self, product,object):
        product_id = f"{object}{product.pk}"
        if object == 'card':
            if product_id not in self.cart.keys():
                self.cart[product_id] = {
                    'pk': product.pk,
                    'cant': 1,
                    'price': float(round(product.price, 2)),
                    'product_name': product.name,
                    'product_rarity':product.get_rarity,
                    'product_version':product.get_version,
                    'product_expantion':product.expantion,
                    'product_type': product.type,
                    'product_image': product.card_images.image_url_small,
                }
            else:
                self.cart[product_id]['cant'] += 1        
                self.cart[product_id]['price'] = float(round(product.price * self.cart[product_id]['cant'], 2))
        elif object == 'deck':
            pass # Decks proccess
        self.save()
        return True
    
    def decrement(self, product,object):
        
        product_id = f"{object}{product.pk}"
        if object == 'card':
            
            if product_id in self.cart.keys():
                self.cart[product_id]['cant'] -= 1
                if self.cart[product_id]['cant'] <= 0:
                    self.remove(product, object)
                    if not self.cart.keys():
                        # Era el último elemento del carrito
                        return redirect('clear_cart_instance')
                else:
                    self.cart[product_id]['price'] = float(round(product.price * self.cart[product_id]['cant'], 2))
                    self.save()
        elif object == 'deck':
            pass # Decks proccess
        return True

    def remove(self, product, object):
        product_id = f"{object}{str(product.id)}"
        if product_id in self.cart:
            del self.cart[product_id]
            if not self.cart.keys():
                # Era el ultimo elemento del carrito 
                #print('Era el uiltimo elemento del carrito')
                return redirect('clear_cart_instance')
            self.save()
    
    def save(self) :
        self.session.modified=True
        
            
    def clear_items(self):
        self.session['cart']={}
        self.session.modified=True
        self.save()
        
    def __iter__(self):      
        cart = self.cart.copy()        
        for item in cart.values():
            item['cant']= item['cant']
            item['price']= item['price']    
            yield item
        