# Generated by Django 5.1.3 on 2024-11-26 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_products_image1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image1',
            field=models.ImageField(default='watch.png', upload_to='product_images/'),
        ),
    ]