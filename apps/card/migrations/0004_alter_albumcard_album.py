# Generated by Django 5.1.3 on 2025-01-08 04:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0003_albumcard_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumcard',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='card.album'),
        ),
    ]
