# Generated by Django 2.2.5 on 2019-11-20 18:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportExportExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz', models.CharField(max_length=254)),
                ('category', models.CharField(max_length=254)),
                ('sub_category', models.CharField(max_length=254)),
                ('figure', models.CharField(default='n', max_length=254)),
                ('content', models.CharField(blank=True, max_length=254)),
                ('explanation', models.CharField(blank=True, max_length=254)),
                ('correct', models.CharField(blank=True, max_length=254)),
                ('answer1', models.CharField(blank=True, max_length=254)),
                ('answer2', models.CharField(blank=True, max_length=254)),
                ('answer3', models.CharField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(default='', editable=False, max_length=255)),
                ('time_limit', models.IntegerField(default=30)),
                ('n_questions', models.PositiveIntegerField(default=5)),
                ('public', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True)),
                ('exam_type', models.CharField(choices=[('exam', 'Exam'), ('elearning', 'E-learning')], default='exam', max_length=15)),
                ('show_answers', models.BooleanField(default=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
