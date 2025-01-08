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
    
    
    class Meta:
        verbose_name = "AlbumCard"
        verbose_name_plural = "AlbumCards"

    def __str__(self):
        return str(self.konami_id)

class CardSet(models.Model):
    set_name = models.CharField(max_length=255)
    set_code = models.CharField(max_length=255)
    set_rarity = models.CharField(max_length=255)
    set_rarity_code = models.CharField(max_length=255)
    set_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.set_name

class CardImage(models.Model):
    card = models.ForeignKey('Card', related_name='card_images', on_delete=models.CASCADE)
    image_url = models.URLField()
    image_url_small = models.URLField()
    image_url_cropped = models.URLField()

class CardPrice(models.Model):
    card = models.ForeignKey('Card', related_name='card_prices', on_delete=models.CASCADE)
    cardmarket_price = models.DecimalField(max_digits=10, decimal_places=2)
    tcgplayer_price = models.DecimalField(max_digits=10, decimal_places=2)
    ebay_price = models.DecimalField(max_digits=10, decimal_places=2)
    amazon_price = models.DecimalField(max_digits=10, decimal_places=2)
    coolstuffinc_price = models.DecimalField(max_digits=10, decimal_places=2)

class Card(models.Model):
    konami_id = models.CharField(null=False, blank=False, default='0', max_length=8)
    name = models.CharField(max_length=255)
    typeline = models.JSONField(null=True, blank=True)
    type = models.CharField(max_length=255)
    humanReadableCardType = models.CharField(max_length=255)
    frameType = models.CharField(max_length=255)
    desc = models.TextField()
    race = models.CharField(max_length=255)
    pend_desc = models.TextField(null=True, blank=True)
    monster_desc = models.TextField(null=True, blank=True)
    atk = models.IntegerField(null=True, blank=True)
    defense = models.IntegerField(null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)
    attribute = models.CharField(null=True, blank=True, max_length=255)
    archetype = models.CharField(max_length=255, null=True, blank=True)
    scale = models.IntegerField(null=True, blank=True)
    linkval = models.IntegerField(null=True, blank=True)
    linkmarkers = models.JSONField(null=True, blank=True)
    ygoprodeck_url = models.URLField()
    card_sets = models.ManyToManyField(CardSet, related_name='cards')
    album_card = models.OneToOneField(AlbumCard, related_name='card', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


    

    
