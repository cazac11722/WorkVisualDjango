from django.contrib import admin
from .models import Task, TaskTimeInfo, TaskPerformance, TaskPoints, ProjectTask

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_by', 'owner', 'created_at')
    search_fields = ('title', 'created_by__username', 'owner__username')
    list_filter = ('created_at', 'updated_at')

@admin.register(TaskTimeInfo)
class TaskTimeInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'start_date', 'end_date', 'start_time', 'end_time', 'duration')
    list_filter = ('start_date', 'end_date')

@admin.register(TaskPerformance)
class TaskPerformanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'progress', 'performance', 'idea_contribution', 'voluntary')

@admin.register(TaskPoints)
class TaskPointsAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'points', 'created_at', 'updated_at')

@admin.register(ProjectTask)
class ProjectTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'title', 'status', 'created_by', 'created_at')
    search_fields = ('title', 'status', 'created_by__username')
    list_filter = ('status', 'created_at')
