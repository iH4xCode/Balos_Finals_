# Generated by Django 5.1.5 on 2025-01-29 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='is_ordered',
            field=models.BooleanField(default=False),
        ),
    ]
