# Generated by Django 4.2.4 on 2023-09-23 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecohiveapp', '0039_cart_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='total_price',
        ),
    ]
