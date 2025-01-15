# Generated by Django 5.1.4 on 2025-01-13 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0009_rename_cup_coin_cup'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='description',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
