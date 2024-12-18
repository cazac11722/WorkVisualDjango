from django.contrib import admin
from .models import Task, TaskTimeInfo, TaskPerformance, TaskPoints

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
    list_display = ('id', 'task', 'progress', 'performance')

@admin.register(TaskPoints)
class TaskPointsAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'points')
