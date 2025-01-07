from django.db import models

from apps.accounts.models import User

# Create your models here.



class Album(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albumes"

    def __str__(self):
        return self.pk


class AlbumCard(models.Model):
    
    

    class Meta:
        verbose_name = "AlbumCard"
        verbose_name_plural = "AlbumCards"

    def __str__(self):
        return self.pk

    

    
