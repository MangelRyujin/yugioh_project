from django.db import models

from apps.accounts.models import User

# Create your models here.

class Album(models.Model):
    
    name = models.CharField(max_length=100, blank=False, null=False, default='Album')
    cardsQuantity = models.PositiveIntegerField(default=0, blank=False, null=False)
    total_price = models.FloatField(default=0.00, blank=True, null=False)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albumes"

    def __str__(self):
        return str(self.name)


class AlbumCard(models.Model):
    
    price = models.FloatField(blank=False, null=False, default=0.00)
    stock = models.PositiveBigIntegerField(default=1, blank=False, null=False)
    konami_id = models.CharField(max_length=8, blank=False, null=False, default='00000000')
    real_image = models.ImageField(upload_to='example/', blank=True, null=True)
    album = models.ForeignKey(Album, related_name='cards', on_delete=models.CASCADE)
    #card = models.OneToOneField(Card, related_name='card', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "AlbumCard"
        verbose_name_plural = "AlbumCards"

    def __str__(self):
        return str(self.konami_id)

    

    
