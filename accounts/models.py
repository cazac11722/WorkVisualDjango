# models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    start_work_time = models.TimeField(null=True, blank=True)
    end_work_time = models.TimeField(null=True, blank=True)
    
    notifications = models.JSONField(default=list)  # 알림 및 설정
    settings = models.JSONField(default=dict)  # 추가 설정 정보
    
    name = models.CharField(max_length=100, null=True, blank=True)
    hire_date = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)

    company_name = models.CharField(max_length=255, null=True, blank=True)
    department = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    current_status = models.CharField(max_length=100, null=True, blank=True)  # 현재 상태 속성 추가
    evaluation = models.JSONField(default=dict, null=True, blank=True)  # 평가 정보 저장 (예: {"리더십": 4, "협업": 5})
    points = models.IntegerField(default=0)  # 포인트 추가
    organization = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} 프로필"

class Organization(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    org_count = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_organizations')
    ranks = models.ManyToManyField('OrganizationRank', related_name='organizations')  # ✅ ManyToManyField
    departments = models.ManyToManyField('OrganizationDepartment', related_name='organizations')  # ✅ ManyToManyField

    def __str__(self):
        return self.name

class OrganizationReason(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

class OrganizationDepartment(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    level = models.CharField(max_length=50)
    permissions = models.JSONField(default=dict, null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

class OrganizationRank(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    level = models.CharField(max_length=50)
    permissions = models.JSONField(default=dict, null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

class OrganizationUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    joined_date = models.DateTimeField(auto_now_add=True)
    department = models.ForeignKey(OrganizationDepartment, on_delete=models.SET_NULL, null=True, blank=True)
    rank = models.ForeignKey(OrganizationRank, on_delete=models.SET_NULL, null=True, blank=True)
    reason = models.JSONField(default=list, null=True, blank=True)

class OrganizationUserPoint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    value = models.IntegerField()
    upload_date = models.DateTimeField(auto_now_add=True)

class OrganizationUserReason(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    reason = models.ForeignKey(OrganizationReason, on_delete=models.CASCADE)
    user_content = models.TextField()
    org_content = models.TextField()
    submission_file = models.FileField(upload_to='reasons/', null=True, blank=True)
    status = models.CharField(max_length=50, choices=[('pending', '대기 중'), ('approved', '승인됨'), ('rejected', '거절됨')])
    upload_date = models.DateTimeField(auto_now_add=True)

class OrganizationProjectScope(models.Model):
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE, related_name='project_scopes')
    name = models.CharField(max_length=100)
    description = models.TextField()
    upload_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class OrganizationProjectType(models.Model):
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE, related_name='project_types')
    name = models.CharField(max_length=100)
    description = models.TextField()
    upload_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class OrganizationGoal(models.Model):
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE, related_name='goals')
    title = models.CharField(max_length=100)
    content = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    goal_type = models.CharField(max_length=50, choices=[
        ('long_term', '장기 목표'),
        ('mid_term', '중기 목표'),
        ('monthly', '월별 실행 목표'),
        ('weekly', '주별 실행 목표'),
    ])
    result = models.TextField(null=True, blank=True)
    upload_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class OrganizationCommonText(models.Model):
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE, related_name='common_texts')
    title = models.CharField(max_length=100)
    content = models.TextField()
    type = models.CharField(max_length=50)
    upload_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.type} - {self.title}"

class OrganizationWorkResult(models.Model):
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE, related_name='work_results')
    title = models.CharField(max_length=100)
    content = models.TextField()
    upload_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField(null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - 출근 {self.check_in} | 퇴근 {self.check_out}"