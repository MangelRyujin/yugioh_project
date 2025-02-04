from django.db import models

from apps.accounts.models import User

# Create your models here.

class AbstractCard(models.Model):
    RARITY_CARD = (
        ('1',"Comun"),
        ('2',"Rare"),
        ('3',"Super rare"),
        ('4',"Ultra rare"),
        ('5',"Secret rare")
    )
    VERSION_CARD = (
        ('1',"TCG"),
        ('2',"OCG")
    )
    ATTRIBUTE_CARD = (
        ('1', 'FIRE'),
        ('2', 'WATER'),
        ('3', 'WIND'),
        ('4', 'EARTH'),
        ('5', 'DARK'),
        ('6', 'LIGHT'),
        ('7', 'DIVINE')
    )
    stock = models.PositiveBigIntegerField(default=1, blank=False, null=False)
    rarity = models.CharField(max_length=1, choices=RARITY_CARD, default='1') 
    version = models.CharField(max_length=1, choices=VERSION_CARD, default='1') 
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
    attribute = models.CharField(null=True, blank=True, max_length=1, choices=ATTRIBUTE_CARD)
    archetype = models.CharField(max_length=255, null=True, blank=True)
    scale = models.IntegerField(null=True, blank=True)
    linkval = models.IntegerField(null=True, blank=True)
    linkmarkers = models.JSONField(null=True, blank=True)
    expantion = models.CharField(max_length=30)
    
    class Meta:
        abstract = True

class AbstractCardImage(models.Model):
    image_url = models.URLField()
    image_url_small = models.URLField()
    image_url_cropped = models.URLField()
    
    class Meta:
        abstract = True


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


class AlbumCard(AbstractCard):
    price = models.FloatField(blank=False, null=False, default=0.00)
    album = models.ForeignKey(Album, related_name='cards', on_delete=models.CASCADE)
    
    
    class Meta:
        verbose_name = "AlbumCard"
        verbose_name_plural = "AlbumCards"

    def __str__(self):
        return str(self.konami_id)    

class CardImage(AbstractCardImage):
    card = models.OneToOneField(AlbumCard, related_name='card_images', on_delete=models.CASCADE)

    def __str__(self):
        return self.card.name


    
class AlbumDecks(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, default='Album')
    description =  models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="album_deck_user")
    image= models.ImageField(upload_to="AlbumDeck",null=True)
    is_active=models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "AlbumDeck"
        verbose_name_plural = "AlbumDecks"

    def __str__(self):
        return str(self.name)
    
    @property
    def total_cards(self):
        return sum(card.stock for card in self.deck_cards.all())
    

class AlbumDecksCard(AbstractCard):
    deck = models.ForeignKey(AlbumDecks, related_name='deck_cards', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "AlbumDecksCard"
        verbose_name_plural = "AlbumDecksCards"

    def __str__(self):
        return str(self.konami_id)    

class DeckCardImage(AbstractCardImage):
    card = models.OneToOneField(AlbumDecksCard, related_name='deck_card_images', on_delete=models.CASCADE)

    def __str__(self):
        return self.card.name