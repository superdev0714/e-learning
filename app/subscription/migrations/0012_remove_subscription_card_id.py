# Generated by Django 2.2.5 on 2021-01-05 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0011_subscription_card_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='card_id',
        ),
    ]
