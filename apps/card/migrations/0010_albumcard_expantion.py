# Generated by Django 5.1.4 on 2025-01-19 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0009_alter_albumcard_rarity_alter_albumcard_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='albumcard',
            name='expantion',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
