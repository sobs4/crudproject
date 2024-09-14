# Generated by Django 5.0.8 on 2024-09-08 09:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=50)),
                ('seats_available', models.IntegerField()),
                ('details', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TutorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('courses', models.ManyToManyField(related_name='tutors', to='course.course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='tutor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.tutorprofile'),
        ),
    ]
