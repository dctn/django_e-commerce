# Generated by Django 5.1.3 on 2024-11-28 06:22

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_alter_products_size'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('product', models.CharField(max_length=500)),
                ('size', models.CharField(max_length=500)),
                ('color', models.CharField(max_length=500)),
                ('quantity', models.IntegerField(null=True,blank=True)),
                ('price', models.IntegerField(null=True,blank=True)),
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=550, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
