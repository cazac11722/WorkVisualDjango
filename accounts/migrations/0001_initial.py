# Generated by Django 5.1.4 on 2025-03-03 10:00

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateTimeField()),
                ('check_out', models.DateTimeField(blank=True, null=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('org_count', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_organizations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationCommonText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('type', models.CharField(max_length=50)),
                ('upload_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='common_texts', to='accounts.organization')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True, null=True)),
                ('level', models.CharField(max_length=50)),
                ('permissions', models.JSONField(blank=True, default=dict, null=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.organization')),
            ],
        ),
        migrations.AddField(
            model_name='organization',
            name='departments',
            field=models.ManyToManyField(related_name='organizations', to='accounts.organizationdepartment'),
        ),
        migrations.CreateModel(
            name='OrganizationGoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('upload_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goals', to='accounts.organization')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationProjectScope',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('upload_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_scopes', to='accounts.organization')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationProjectType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('upload_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_types', to='accounts.organization')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationRank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('level', models.CharField(max_length=50)),
                ('permissions', models.JSONField(blank=True, default=dict, null=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.organization')),
            ],
        ),
        migrations.AddField(
            model_name='organization',
            name='ranks',
            field=models.ManyToManyField(related_name='organizations', to='accounts.organizationrank'),
        ),
        migrations.CreateModel(
            name='OrganizationReason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True, null=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.organization')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined_date', models.DateTimeField(auto_now_add=True)),
                ('reason', models.JSONField(blank=True, default=list, null=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.organizationdepartment')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.organization')),
                ('rank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.organizationrank')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationUserPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.organization')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationUserReason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_content', models.TextField()),
                ('org_content', models.TextField()),
                ('submission_file', models.FileField(blank=True, null=True, upload_to='reasons/')),
                ('status', models.CharField(choices=[('pending', '대기 중'), ('approved', '승인됨'), ('rejected', '거절됨')], max_length=50)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.organization')),
                ('reason', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.organizationreason')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationWorkResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('upload_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_results', to='accounts.organization')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('position', models.CharField(blank=True, max_length=100, null=True)),
                ('start_work_time', models.TimeField(blank=True, null=True)),
                ('end_work_time', models.TimeField(blank=True, null=True)),
                ('notifications', models.JSONField(default=list)),
                ('settings', models.JSONField(default=dict)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('hire_date', models.DateField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True)),
                ('company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('department', models.CharField(blank=True, max_length=255, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('current_status', models.CharField(blank=True, max_length=100, null=True)),
                ('evaluation', models.JSONField(blank=True, default=dict, null=True)),
                ('points', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
