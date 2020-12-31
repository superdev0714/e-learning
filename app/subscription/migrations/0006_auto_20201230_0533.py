# Generated by Django 2.2.5 on 2020-12-30 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0005_auto_20201229_1351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activitylog',
            name='response_details',
        ),
        migrations.AddField(
            model_name='activitylog',
            name='log_detail',
            field=models.CharField(blank=True, help_text='Response Detail', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='status',
            field=models.CharField(choices=[('active', 'ACTIVE'), ('cancelled', 'CANCELLED'), ('halted', 'HALTED'), ('inactive', 'INACTIVE')], default='inactive', help_text='The status subscription of the user', max_length=150),
        ),
    ]