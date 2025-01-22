from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.


class User(AbstractUser):
    phone_number = models.PositiveIntegerField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    
class Donation(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT,null=True,blank=True)
    amount= models.FloatField(validators=[MinValueValidator(1)])
    code = models.CharField(max_length=60)
    create_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    