# Generated by Django 5.1.3 on 2024-11-27 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_colors_alter_products_id_products_colors'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='Size',
            field=models.CharField(default='medium', max_length=550),
        ),
        migrations.AddField(
            model_name='cart',
            name='color',
            field=models.CharField(default='', max_length=550),
        ),
    ]
