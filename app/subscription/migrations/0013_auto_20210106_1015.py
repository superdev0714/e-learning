# Generated by Django 2.2.5 on 2021-01-06 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0012_remove_subscription_card_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='status',
            field=models.CharField(choices=[('active', 'ACTIVE'), ('canceled', 'CANCELLED'), ('past_due', 'PAST_DUE'), ('unpaid', 'UNPAID'), ('incomplete', 'INCOMPLETE'), ('incomplete_expired', 'INCOMPLETE_EXPIRED'), ('inactive', 'INACTIVE')], default='unpaid', help_text='The status subscription of the user', max_length=150),
        ),
    ]