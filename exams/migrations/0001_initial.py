# Generated by Django 2.2.12 on 2021-09-23 20:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('exam_id', models.CharField(max_length=5, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('exam_name', models.CharField(max_length=120)),
                ('semester', models.PositiveIntegerField()),
                ('date_and_time', models.DateTimeField()),
                ('duration', models.PositiveIntegerField(help_text='Exam Duration in Minutes')),
                ('total_questions', models.PositiveIntegerField(help_text='Total Number of Questions in Exam')),
                ('total_assigned_marks', models.PositiveIntegerField(help_text='Total Assigned Marks')),
                ('pass_mark', models.PositiveIntegerField(help_text='Required Score to Pass Exam')),
            ],
            options={
                'verbose_name_plural': 'Exams',
            },
        ),
    ]