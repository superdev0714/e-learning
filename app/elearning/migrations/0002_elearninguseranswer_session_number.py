# Generated by Django 2.2.5 on 2019-09-27 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='elearninguseranswer',
            name='session_number',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
