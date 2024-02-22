# Generated by Django 5.0.1 on 2024-02-08 06:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecohiveapp', '0076_alter_deliveryagent_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_at', models.DateTimeField(auto_now_add=True)),
                ('delivery_agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecohiveapp.deliveryagent')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecohiveapp.order')),
            ],
        ),
    ]