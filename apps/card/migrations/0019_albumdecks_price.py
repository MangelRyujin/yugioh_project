# Generated by Django 5.1.4 on 2025-02-05 01:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0018_alter_albumdecks_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='albumdecks',
            name='price',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
