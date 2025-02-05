# Generated by Django 5.1.4 on 2025-02-03 12:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0013_rename_tipo_albumcard_type'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumDecks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Album', max_length=100)),
                ('description', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albumes',
            },
        ),
        migrations.CreateModel(
            name='AlbumDecksCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.PositiveBigIntegerField(default=1)),
                ('rarity', models.CharField(choices=[('1', 'Comun'), ('2', 'Rare'), ('3', 'Super rare'), ('4', 'Ultra rare'), ('5', 'Secret rare')], default='1', max_length=1)),
                ('version', models.CharField(choices=[('1', 'TCG'), ('2', 'OCG')], default='1', max_length=1)),
                ('konami_id', models.CharField(default='0', max_length=8)),
                ('name', models.CharField(max_length=255)),
                ('typeline', models.JSONField(blank=True, null=True)),
                ('type', models.CharField(max_length=255)),
                ('humanReadableCardType', models.CharField(max_length=255)),
                ('frameType', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('race', models.CharField(max_length=255)),
                ('pend_desc', models.TextField(blank=True, null=True)),
                ('monster_desc', models.TextField(blank=True, null=True)),
                ('atk', models.IntegerField(blank=True, null=True)),
                ('defense', models.IntegerField(blank=True, null=True)),
                ('level', models.IntegerField(blank=True, null=True)),
                ('attribute', models.CharField(blank=True, choices=[('1', 'FIRE'), ('2', 'WATER'), ('3', 'WIND'), ('4', 'EARTH'), ('5', 'DARK'), ('6', 'LIGHT'), ('7', 'DIVINE')], max_length=1, null=True)),
                ('archetype', models.CharField(blank=True, max_length=255, null=True)),
                ('scale', models.IntegerField(blank=True, null=True)),
                ('linkval', models.IntegerField(blank=True, null=True)),
                ('linkmarkers', models.JSONField(blank=True, null=True)),
                ('expantion', models.CharField(max_length=30)),
                ('deck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deck_cards', to='card.albumdecks')),
            ],
            options={
                'verbose_name': 'AlbumDecksCard',
                'verbose_name_plural': 'AlbumDecksCards',
            },
        ),
        migrations.CreateModel(
            name='DeckCardImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField()),
                ('image_url_small', models.URLField()),
                ('image_url_cropped', models.URLField()),
                ('card', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='deck_card_images', to='card.albumdeckscard')),
            ],
        ),
    ]
