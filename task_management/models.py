from django.db import models

# 업무 카테고리
class TaskCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)  # 카테고리 이름
    description = models.TextField(null=True, blank=True)  # 카테고리 설명
    created_at = models.DateTimeField(auto_now_add=True)  # 생성일
    updated_at = models.DateTimeField(auto_now=True)  # 수정일

    def __str__(self):
        return self.name

# 업무 상태
class TaskStatus(models.Model):
    category = models.ForeignKey(TaskCategory, on_delete=models.CASCADE, related_name='statuses')  # 업무 카테고리와 1:N 관계
    name = models.CharField(max_length=255)  # 상태 이름
    description = models.TextField(null=True, blank=True)  # 상태 설명
    created_at = models.DateTimeField(auto_now_add=True)  # 생성일
    updated_at = models.DateTimeField(auto_now=True)  # 수정일

    def __str__(self):
        return f"{self.name} ({self.category.name})"

# 업무 제목
class TaskTitle(models.Model):
    category = models.ForeignKey(TaskCategory, on_delete=models.CASCADE, related_name='titles')  # 업무 카테고리와 1:N 관계
    name = models.CharField(max_length=255)  # 제목 이름
    description = models.TextField(null=True, blank=True)  # 제목 설명
    created_at = models.DateTimeField(auto_now_add=True)  # 생성일
    updated_at = models.DateTimeField(auto_now=True)  # 수정일

    def __str__(self):
        return f"{self.name} ({self.category.name})"

# 업무 내용
class TaskContent(models.Model):
    category = models.ForeignKey(TaskCategory, on_delete=models.CASCADE, related_name='contents')  # 업무 카테고리와 1:N 관계
    content = models.TextField()  # 업무 내용
    details = models.TextField(null=True, blank=True)  # 업무 세부 내용
    created_at = models.DateTimeField(auto_now_add=True)  # 생성일
    updated_at = models.DateTimeField(auto_now=True)  # 수정일

    def __str__(self):
        return f"{self.content[:50]}... ({self.category.name})"

# 업무 예상 소요 시간
class TaskEstimatedTime(models.Model):
    category = models.ForeignKey(TaskCategory, on_delete=models.CASCADE, related_name='estimated_times')  # 업무 카테고리와 1:N 관계
    estimated_time = models.FloatField()  # 예상 소요 시간 (시간 단위)
    created_at = models.DateTimeField(auto_now_add=True)  # 생성일
    updated_at = models.DateTimeField(auto_now=True)  # 수정일

    def __str__(self):
        return f"{self.category.name}: {self.estimated_time} hours"
