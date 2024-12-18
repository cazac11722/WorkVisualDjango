from django.contrib import admin
from .models import TaskCategory, TaskStatus, TaskTitle, TaskContent, TaskEstimatedTime

# TaskCategory 관리자 페이지 설정
@admin.register(TaskCategory)
class TaskCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at', 'updated_at')  # 목록에 표시할 필드
    search_fields = ('name',)  # 검색 가능한 필드
    list_filter = ('created_at', 'updated_at')  # 필터링 옵션
    ordering = ('name',)  # 정렬 기준

# TaskStatus 관리자 페이지 설정
@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'category__name')  # 검색 가능한 필드
    list_filter = ('category', 'created_at')  # 필터링 옵션
    ordering = ('category', 'name')  # 정렬 기준

# TaskTitle 관리자 페이지 설정
@admin.register(TaskTitle)
class TaskTitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'category__name')
    list_filter = ('category', 'created_at')
    ordering = ('category', 'name')

# TaskContent 관리자 페이지 설정
@admin.register(TaskContent)
class TaskContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'category', 'details', 'created_at', 'updated_at')
    search_fields = ('content', 'category__name')
    list_filter = ('category', 'created_at')
    ordering = ('category', 'content')

# TaskEstimatedTime 관리자 페이지 설정
@admin.register(TaskEstimatedTime)
class TaskEstimatedTimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'estimated_time', 'created_at', 'updated_at')
    search_fields = ('category__name',)
    list_filter = ('category',)
    ordering = ('category', 'estimated_time')
