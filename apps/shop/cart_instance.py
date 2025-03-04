from decimal import Decimal
from django.conf import settings 
from django.contrib import messages


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
            self.remove(product)
        else:
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
        self.save()
        return True
    
    def  add_message_product(self, product,message):
        product_id = str(product.id)
        
        if product_id not in self.cart.keys():
            pass
        else:
            self.cart[product_id]['message'] = message or ''
        self.save()
        return True
    
    def increment(self,product):
        product_id = str(product.id)
        if product_id not in self.cart.keys():
                self.cart[product_id] = {
                    'pk':product.pk,
                    'cant': 1,
                    'price': float(round((product.price - (product.price*product.discount)/100),2)),
                    'product_name': product.name,
                    'product_image': product.image_one.url,
                    'message':'',
                    }
        else:
                self.cart[product_id]['cant'] = self.cart[product_id]['cant'] + 1
                self.cart[product_id]['price'] = float(round((product.price - (product.price*product.discount)/100) * self.cart[product_id]['cant'],2))
        self.save()
        return True
    
    def decrement(self,product):
        product_id = str(product.id)
        if self.cart[product_id]['cant'] == 1:
                self.remove(product)
        else:
                self.cart[product_id]['cant'] = self.cart[product_id]['cant'] -1
                self.cart[product_id]['price'] = float(round((product.price - (product.price*product.discount)/100) * self.cart[product_id]['cant'],2))
        self.save()
        return True
    

        
    def remove(self, product,object):
         product_id = f"{object}{str(product.id)}"
         if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    
    def save(self) :
        self.session.modified=True
        
    
            
    def clear_items(self):
        self.session['cart']={}
        self.session.modified=True
        
    def __iter__(self):      
        cart = self.cart.copy()        
        for item in cart.values():
            item['cant']= item['cant']
            item['price']= item['price']    
            yield item
        