# Generated by Django 5.1.4 on 2025-01-31 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0012_rename_type_albumcard_tipo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='albumcard',
            old_name='tipo',
            new_name='type',
        ),
    ]
