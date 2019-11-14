# Generated by Django 2.2.5 on 2019-09-25 08:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='examusersession',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='examuseranswer',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.Answer'),
        ),
        migrations.AddField(
            model_name='examuseranswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.Question'),
        ),
        migrations.AddField(
            model_name='examuseranswer',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.ExamUserSession'),
        ),
        migrations.AddField(
            model_name='examuseranswer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='question.Question'),
        ),
    ]
