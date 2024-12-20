from django.db import models
from django.contrib.auth.models import User

# 업무 테이블
class Task(models.Model):
    title = models.CharField(max_length=255)  # 업무 제목
    description = models.TextField()  # 상세 업무 내용
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_created')  # 생성자
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_owned')  # 업무 담당자
    planner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_planned', null=True, blank=True)  # 업무 기획자
    links = models.TextField(null=True, blank=True)  # 관련 링크
    created_at = models.DateTimeField(auto_now_add=True)  # 생성일
    updated_at = models.DateTimeField(auto_now=True)  # 수정일

    def __str__(self):
        return self.title


# 시간 정보 테이블
class TaskTimeInfo(models.Model):
    task = models.OneToOneField(Task, on_delete=models.CASCADE, related_name='time_info')  # 업무와 1:1 관계
    start_date = models.DateField()  # 시작 날짜
    end_date = models.DateField(null=True, blank=True)  # 종료 날짜 (선택적 입력)
    start_time = models.TimeField()  # 시작 시간
    end_time = models.TimeField(null=True, blank=True)  # 종료 시간 (선택적 입력)
    duration = models.FloatField(null=True, blank=True)  # 소요 시간

    def __str__(self):
        return f"Time Info for Task: {self.task.title}"


# 성과 테이블
class TaskPerformance(models.Model):
    task = models.OneToOneField(Task, on_delete=models.CASCADE, related_name='performance')  # 업무와 1:1 관계
    progress = models.FloatField(default=0.0)  # 진행률
    performance = models.FloatField(default=0.0)  # 성과
    delays = models.TextField(null=True, blank=True)  # 지연 이유
    idea_contribution = models.FloatField(default=0.0)  # 아이디어 기여도
    voluntary = models.BooleanField(default=False)  # 자발성

    def __str__(self):
        return f"Performance for Task: {self.task.title}"


# 포인트 테이블
class TaskPoints(models.Model):
    task = models.OneToOneField(Task, on_delete=models.CASCADE, related_name='points')  # 업무와 1:1 관계
    points = models.IntegerField(default=0)  # 부여된 포인트
    created_at = models.DateTimeField(auto_now_add=True)  # 포인트 생성일
    updated_at = models.DateTimeField(auto_now=True)  # 포인트 수정일

    def __str__(self):
        return f"Points for Task: {self.task.title} - {self.points} pts"

# 업무 테이블
class ProjectTask(models.Model):
    STATUS_CHOICES = [
        ("In Progress", "진행 중"),
        ("Completed", "완료"),
        ("Pending", "보류중"),
        ("On Hold", "홀딩"),
    ]

    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='project')  # 업무와 1:1 관계
    title = models.CharField(max_length=255)  # 업무 제목
    work_contents = models.TextField()  # 업무기획-내용
    work_details = models.TextField(null=True, blank=True)  # 상세 업무 내용
    reason_delay = models.TextField(null=True, blank=True)  # 지연사유
    link = models.TextField(null=True, blank=True)  # 관련 링크
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")  # 상태
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_tasks_created')  # 생성자
    start_time = models.TimeField(null=True,  blank=True)  # 시작 시간
    end_time = models.TimeField(null=True, blank=True)  # 종료 시간 (선택적 입력)
    created_at = models.DateTimeField(auto_now_add=True)  # 생성일
    updated_at = models.DateTimeField(auto_now=True)  # 수정일

    def __str__(self):
        return self.title