from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from solo.models import SingletonModel
# Create your models here.

class Coin(SingletonModel):
    cup = models.FloatField(default=1,validators=[MinValueValidator(0.01)])
    

    class Meta:
        verbose_name = "Coin"
        verbose_name_plural = "Coins"
    
    def __str__(self):
        return f'{self.pk}' 
    
class Subscription(models.Model):
    name = models.CharField(max_length=30,unique=True)
    description = models.CharField(max_length=100, default="")
    popular=models.BooleanField(default=False)
    month_price = models.FloatField(validators=[MinValueValidator(0.01)])
    annual_price_discount = models.PositiveIntegerField(default=0,validators=[MaxValueValidator(100)])

    class Meta:
        verbose_name = "Subscription"
        verbose_name_plural = "Subscriptions"

    def __str__(self):
        return self.name
    
    @property
    def month_price_CUP(self):
        cup = Coin.objects.first()
        if self.month_price:
            return self.month_price * cup.cup
        return 0
    
    @property
    def discount_anual_price(self):
        if self.month_price:
            if self.annual_price_discount:
                if self.annual_price_discount > 0:
                    return round(self.month_price * 12 - ( (self.month_price * 12) * self.annual_price_discount ) /100 ,2 )
            else:   
                return round(self.month_price * 12 ,2 )     
        return 0
    
    @property
    def discount_anual_price_cup(self):
        cup = Coin.objects.first()
        return round(self.discount_anual_price * cup.cup , 2)
    
class FeatureSubscription(models.Model):
    name = models.CharField(max_length=255)
    subscription = models.ForeignKey(Subscription,on_delete=models.CASCADE,verbose_name='feature_subscription',related_name='feature_subscription')

    class Meta:
        verbose_name = "Feature of Subscription"
        verbose_name_plural = "Features of Subscription"

    def __str__(self):
        return self.name


