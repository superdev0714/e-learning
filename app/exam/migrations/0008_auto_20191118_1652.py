# Generated by Django 2.2.5 on 2019-11-18 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0007_merge_20191118_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importexportexam',
            name='explanation',
            field=models.TextField(blank=True),
        ),
    ]