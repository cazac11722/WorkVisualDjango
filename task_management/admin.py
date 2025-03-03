# admin.py
from django.contrib import admin
from .models import Task, Goal, TaskChat

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'upload_date', 'modified_date', 'progress')
    search_fields = ('title', 'author__username')

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_date', 'end_date', 'goal_type', 'organizer', 'upload_date', 'modified_date')
    search_fields = ('content', 'organizer__username')

@admin.register(TaskChat)
class TaskChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'user', 'message', 'timestamp')
    search_fields = ('task__title', 'user__username', 'message')
