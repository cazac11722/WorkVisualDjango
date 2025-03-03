# models.py
from django.db import models
from django.contrib.auth.models import User
from accounts.models import Organization  # accounts 앱에서 Organization 가져오기
import uuid

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owned_tasks", null=True, blank=True)  # 실제 소유자
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="tasks", null=True, blank=True)  # 조직

    upload_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    progress = models.CharField(max_length=100, null=True, blank=True)
    attributes = models.JSONField(default=dict, null=True, blank=True)
    table_head = models.JSONField(default=list, null=True, blank=True)  # 테이블 헤더 데이터 저장
    table_body = models.JSONField(default=list, null=True, blank=True)  # 테이블 본문 데이터 저장
    
    def __str__(self):
        return self.title

class Goal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    start_date = models.DateField()
    end_date = models.DateField()
    goal_type = models.CharField(max_length=50, choices=[
        ('long_term', '장기 목표'),
        ('mid_term', '중기 목표'),
        ('monthly', '월별 실행 목표'),
        ('weekly', '주별 실행 목표'),
    ])
    content = models.TextField()
    result = models.TextField(null=True, blank=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content[:50]

class TaskChat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='chats')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}: {self.message[:50]}"