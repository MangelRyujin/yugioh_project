from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from apps.accounts.models import User
# Create your models here.


class Order(models.Model):
    create_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='create_user')
    current_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='current_user')
    current_destination = models.CharField(max_length=120)
    delivery = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f'{self.pk}'

class Item(models.Model):
    STATE_CARD = (
        ('1',"Procesando"),
        ('2',"Pagada"),
    )
    state = models.CharField(max_length=1, choices=STATE_CARD, default='1') 
    delivery = models.BooleanField(default=False)
    create_date_at = models.DateField(auto_now=True)
    create_time_at = models.TimeField(auto_now=True)
    delivery_date = models.DateField(blank=True,null =True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller')
    final_destination = models.CharField(max_length=120)
    price = models.FloatField()
    cant = models.PositiveIntegerField(default=1)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order',null=True,blank=True)
    

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        return f'{self.pk}'

    