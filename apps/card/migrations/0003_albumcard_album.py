# Generated by Django 5.1.3 on 2025-01-08 04:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0002_album_cardsquantity_album_name_album_total_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='albumcard',
            name='album',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='card.album'),
        ),
    ]
