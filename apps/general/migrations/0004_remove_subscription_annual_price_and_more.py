# Generated by Django 5.1.4 on 2025-01-13 01:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_rename_price_subscription_annual_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='annual_price',
        ),
        migrations.AddField(
            model_name='subscription',
            name='annual_price_discount',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)]),
            preserve_default=False,
        ),
    ]
