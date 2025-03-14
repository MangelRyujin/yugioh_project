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
            elif object == 'deck':
                
                if product_id not in self.cart.keys():
                    self.cart[product_id] = {
                        'pk': product.pk,
                        'object': object,
                        'cant': 1,
                        'price': product.price,
                        'total_cards': product.total_cards,
                        'product_name': product.name,
                        'product_image': product.image.url if product.image else None,
                    }
                    
                
                else:
                    
                    self.cart[product_id]['cant'] = 1
                    self.cart[product_id]['price'] = product.price 
            else:
                pass
        self.save()
        return True
    
   
    # def increment(self, product,object):
    #     product_id = f"{object}{product.pk}"
    #     if object == 'card':
    #         if product_id not in self.cart.keys():
    #             self.cart[product_id] = {
    #                 'pk': product.pk,
    #                 'cant': 1,
    #                 'price': float(round(product.price, 2)),
    #                 'product_name': product.name,
    #                 'product_rarity':product.get_rarity,
    #                 'product_version':product.get_version,
    #                 'product_expantion':product.expantion,
    #                 'product_type': product.type,
    #                 'product_image': product.card_images.image_url_small,
    #             }
    #         else:
    #             self.cart[product_id]['cant'] += 1        
    #             self.cart[product_id]['price'] = float(round(product.price * self.cart[product_id]['cant'], 2))
    #     elif object == 'deck':
    #         pass # Decks proccess
    #     self.save()
    #     return True
    
    def increment(self, product, object):
        product_id = f"{object}{product.pk}"
        if object == 'card':
            if product_id not in self.cart.keys():
                if product.stock >= 1:
                    self.cart[product_id] = {
                        'pk': product.pk,
                        'cant': 1,
                        'price': float(round(product.price, 2)),
                        'product_name': product.name,
                        'product_rarity': product.get_rarity,
                        'product_version': product.get_version,
                        'product_expantion': product.expantion,
                        'product_type': product.type,
                        'product_image': product.card_images.image_url_small,
                    }
                else:
                    return False  # No hay suficiente stock
            else:
                if self.cart[product_id]['cant'] < product.stock:
                    self.cart[product_id]['cant'] += 1
                    self.cart[product_id]['price'] = float(round(product.price * self.cart[product_id]['cant'], 2))
                else:
                    return False  # No hay suficiente stock
        elif object == 'deck':
            pass  # Proceso para decks
        self.save()
        return True
    
    def decrement(self, product,object):
        
        product_id = f"{object}{product.pk}"
        if object == 'card':
            
            if product_id in self.cart.keys():
                self.cart[product_id]['cant'] -= 1
                if self.cart[product_id]['cant'] <= 0:
                    self.remove(product, object)
                else:
                    self.cart[product_id]['price'] = float(round(product.price * self.cart[product_id]['cant'], 2))
                    self.save()
        elif object == 'deck':
            pass # Decks proccess
        return True

    def remove(self, product, object):
        product_id = f"{object}{product.id}"
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    
    def last_element(self):
        if len(self.cart) == 1:
            for item in self.cart.values():
                if item['cant'] == 1:
                    return True
        return False

    
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
        