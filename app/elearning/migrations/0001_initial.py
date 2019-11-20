# Generated by Django 2.2.5 on 2019-11-20 18:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exam', '0001_initial'),
        ('question', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ELearning',
            fields=[
                ('exam_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='exam.Exam')),
                ('slides', models.BooleanField(default=False)),
                ('random_questions', models.BooleanField(default=True)),
                ('certificate_count', models.PositiveSmallIntegerField(default=369)),
            ],
            bases=('exam.exam',),
        ),
        migrations.CreateModel(
            name='ELearningSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(default=0)),
                ('elearning', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sessions', to='elearning.ELearning')),
                ('questions', models.ManyToManyField(blank=True, to='question.Question')),
            ],
        ),
        migrations.CreateModel(
            name='ImportExportELearning',
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
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slides/')),
                ('elearning', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='elearning.ELearning')),
            ],
        ),
        migrations.CreateModel(
            name='ELearningUserSession',
            fields=[
                ('examusersession_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='question.ExamUserSession')),
                ('seen_slides', models.PositiveIntegerField(default=0)),
                ('phase', models.IntegerField(choices=[(0, 'Corrections'), (1, 'Repetitions'), (2, 'New Questions'), (3, 'Slides')], default=2)),
                ('memory_force', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='medium', max_length=100)),
                ('active_session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='elearning.ELearningSession')),
                ('elearning', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning.ELearning')),
            ],
            bases=('question.examusersession',),
        ),
        migrations.CreateModel(
            name='ELearningUserAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_number', models.PositiveIntegerField(default=0)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.Answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.Question')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='elearning.ELearningUserSession')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='elearningsession',
            name='slides',
            field=models.ManyToManyField(blank=True, to='elearning.Slide'),
        ),
        migrations.CreateModel(
            name='ELearningRepetition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('repeat_after', models.DateField()),
                ('answered', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.Question')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning.ELearningUserSession')),
            ],
        ),
        migrations.CreateModel(
            name='ELearningCorrection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.Question')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning.ELearningUserSession')),
            ],
        ),
    ]
