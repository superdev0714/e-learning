# Generated by Django 2.2.5 on 2021-01-06 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210106_0433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, help_text='username of the user', max_length=254, null=True),
        ),
    ]
