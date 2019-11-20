# Generated by Django 2.2.5 on 2019-11-19 10:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('question', '0001_initial'),
        ('elearning', '0002_auto_20191119_1016'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='elearninguseranswer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='elearningsession',
            name='elearning',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sessions', to='elearning.ELearning'),
        ),
        migrations.AddField(
            model_name='elearningsession',
            name='questions',
            field=models.ManyToManyField(blank=True, to='question.Question'),
        ),
        migrations.AddField(
            model_name='elearningsession',
            name='slides',
            field=models.ManyToManyField(blank=True, to='elearning.Slide'),
        ),
        migrations.AddField(
            model_name='elearningrepetition',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.Question'),
        ),
        migrations.AddField(
            model_name='elearningrepetition',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning.ELearningUserSession'),
        ),
        migrations.AddField(
            model_name='elearningcorrection',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.Question'),
        ),
        migrations.AddField(
            model_name='elearningcorrection',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning.ELearningUserSession'),
        ),
    ]
