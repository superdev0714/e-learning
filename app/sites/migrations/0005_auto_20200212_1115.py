# Generated by Django 2.2.5 on 2020-02-12 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Uploading', '0004_auto_20200211_0552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimage',
            name='image',
            field=models.ImageField(upload_to='static/img/'),
        ),
        migrations.AlterModelTable(
            name='uploadmedia',
            table='Uploading Slides',
        ),
    ]