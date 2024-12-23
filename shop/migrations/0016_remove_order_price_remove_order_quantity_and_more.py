# Generated by Django 5.1.3 on 2024-11-29 14:25

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_cart_id_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='products',
            name='image1',
            field=django_resized.forms.ResizedImageField(crop=None, default='watch.png', force_format=None, keep_meta=True, quality=-1, scale=None, size=[1920, 1080], upload_to='product_images/'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image2',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[1920, 1080], upload_to='product_images/'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image3',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[1920, 1080], upload_to='product_images/'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image4',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[1920, 1080], upload_to='product_images/'),
        ),
    ]
