# Generated by Django 2.2.5 on 2020-12-23 10:56

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200311_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='stripe_customer',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True),
        ),
    ]
