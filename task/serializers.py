from rest_framework import serializers
from .models import Task, TaskTimeInfo, TaskPerformance, TaskPoints, ProjectTask

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskTimeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskTimeInfo
        fields = '__all__'

class TaskPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskPerformance
        fields = '__all__'

class TaskPointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskPoints
        fields = '__all__'

class ProjectTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTask
        fields = '__all__'
