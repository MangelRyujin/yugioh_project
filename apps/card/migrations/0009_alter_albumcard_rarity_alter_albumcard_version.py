# Generated by Django 5.1.4 on 2025-01-13 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0008_alter_albumcard_rarity_alter_albumcard_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumcard',
            name='rarity',
            field=models.CharField(choices=[('1', 'Comun'), ('2', 'Rare'), ('3', 'Super rare'), ('4', 'Ultra rare'), ('5', 'Secret rare')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='albumcard',
            name='version',
            field=models.CharField(choices=[('1', 'TCG'), ('2', 'OCG')], default='1', max_length=1),
        ),
    ]
