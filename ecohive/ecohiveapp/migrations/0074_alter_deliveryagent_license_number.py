# Generated by Django 5.0.1 on 2024-01-31 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecohiveapp', '0073_alter_deliveryagent_license_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryagent',
            name='license_number',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]