# Generated by Django 5.1.4 on 2025-02-05 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0019_albumdecks_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumdecks',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='AlbumDeck'),
        ),
    ]
