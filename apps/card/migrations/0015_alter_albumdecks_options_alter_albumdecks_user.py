# Generated by Django 5.1.4 on 2025-02-03 13:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0014_albumdecks_albumdeckscard_deckcardimage'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='albumdecks',
            options={'verbose_name': 'AlbumDeck', 'verbose_name_plural': 'AlbumDecks'},
        ),
        migrations.AlterField(
            model_name='albumdecks',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album_deck_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
