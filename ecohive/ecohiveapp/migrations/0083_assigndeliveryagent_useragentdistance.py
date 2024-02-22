# Generated by Django 5.0.1 on 2024-02-20 06:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecohiveapp', '0082_alter_billingdetails_latitude_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assigndeliveryagent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('billingdetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecohiveapp.billingdetails')),
                ('deliveryagent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecohiveapp.deliveryagent')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecohiveapp.order')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecohiveapp.seller')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserAgentDistance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.FloatField(blank=True, null=True)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecohiveapp.deliveryagent')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'agent')},
            },
        ),
    ]
