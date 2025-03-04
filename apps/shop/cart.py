from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from apps.accounts.models import User

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Cart of {self.user.username}'

    def add_item(self, content_object, quantity=1):
        content_type = ContentType.objects.get_for_model(content_object)
        cart_item, created = CartItem.objects.get_or_create(
            cart=self,
            content_type=content_type,
            object_id=content_object.id,
            defaults={'quantity': quantity}
        )
        if not created:
            cart_item.quantity += quantity
            cart_item.save()

    def remove_item(self, content_object):
        content_type = ContentType.objects.get_for_model(content_object)
        CartItem.objects.filter(
            cart=self,
            content_type=content_type,
            object_id=content_object.id
        ).delete()

    def clear_cart(self):
        self.items.all().delete()

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())

    def increase_quantity(self, content_object, quantity=1):
        content_type = ContentType.objects.get_for_model(content_object)
        cart_item = CartItem.objects.get(
            cart=self,
            content_type=content_type,
            object_id=content_object.id
        )
        cart_item.quantity += quantity
        cart_item.save()

    def decrease_quantity(self, content_object, quantity=1):
        content_type = ContentType.objects.get_for_model(content_object)
        cart_item = CartItem.objects.get(
            cart=self,
            content_type=content_type,
            object_id=content_object.id
        )
        if cart_item.quantity > quantity:
            cart_item.quantity -= quantity
            cart_item.save()
        else:
            cart_item.delete()

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.content_object}'

    def get_total_price(self):
        return self.content_object.price * self.quantity