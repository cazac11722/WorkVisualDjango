# Generated by Django 5.1.4 on 2024-12-18 20:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('links', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks_created', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks_owned', to=settings.AUTH_USER_MODEL)),
                ('planner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks_planned', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TaskPerformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress', models.FloatField(default=0.0)),
                ('performance', models.FloatField(default=0.0)),
                ('delays', models.TextField(blank=True, null=True)),
                ('idea_contribution', models.FloatField(default=0.0)),
                ('voluntary', models.BooleanField(default=False)),
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='performance', to='task.task')),
            ],
        ),
        migrations.CreateModel(
            name='TaskPoints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='points', to='task.task')),
            ],
        ),
        migrations.CreateModel(
            name='TaskTimeInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('duration', models.FloatField(blank=True, null=True)),
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='time_info', to='task.task')),
            ],
        ),
    ]