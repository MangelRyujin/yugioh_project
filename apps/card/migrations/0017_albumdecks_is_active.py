# Generated by Django 5.1.4 on 2025-02-04 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0016_albumdecks_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='albumdecks',
            name='is_active',
            field=models.FloatField(default=False),
        ),
    ]
