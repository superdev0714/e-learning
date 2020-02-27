# Generated by Django 2.2.5 on 2020-02-04 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elearning', models.CharField(help_text='elearning of the presentation', max_length=500)),
                ('topic', models.CharField(help_text='topic of the presentation', max_length=500)),
                ('slide', models.CharField(help_text='name of the slide', max_length=1000)),
                ('is_demo', models.BooleanField(default=False)),
            ],
        ),
    ]