# Generated by Django 2.2.5 on 2019-12-16 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0003_auto_20191213_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='elearning',
            field=models.CharField(help_text='elearning of the presentation', max_length=500),
        ),
    ]
