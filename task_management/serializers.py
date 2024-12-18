from rest_framework import serializers
from .models import TaskCategory, TaskStatus, TaskTitle, TaskContent, TaskEstimatedTime

class TaskCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskCategory
        fields = '__all__'

class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = '__all__'

class TaskTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskTitle
        fields = '__all__'

class TaskContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskContent
        fields = '__all__'

class TaskEstimatedTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskEstimatedTime
        fields = '__all__'
