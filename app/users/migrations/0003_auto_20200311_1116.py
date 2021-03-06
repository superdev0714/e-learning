# Generated by Django 2.2.5 on 2020-03-11 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_is_demo'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='manager',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='member_type',
            field=models.CharField(choices=[('Team Member', 'Team Member'), ('Manager', 'Manager')], default=0, max_length=254),
        ),
    ]
