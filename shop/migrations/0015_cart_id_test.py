# Generated by Django 5.1.3 on 2024-11-28 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='id_test',
            field=models.CharField(default='', editable=False, max_length=50),
        ),
    ]
