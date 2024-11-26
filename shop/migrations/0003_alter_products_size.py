# Generated by Django 5.1.3 on 2024-11-26 07:09

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_products_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='size',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')], default='md', max_length=255),
        ),
    ]
