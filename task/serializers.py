from rest_framework import serializers
from .models import Task, TaskTimeInfo, TaskPerformance, TaskPoints

# Task Serializer
class TaskSerializer(serializers.ModelSerializer):
    created_by_username = serializers.ReadOnlyField(source='created_by.username')  # 생성자 이름
    owner_username = serializers.ReadOnlyField(source='owner.username')  # 담당자 이름

    class Meta:
        model = Task
        fields = '__all__'

# TaskTimeInfo Serializer
class TaskTimeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskTimeInfo
        fields = '__all__'

# TaskPerformance Serializer
class TaskPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskPerformance
        fields = '__all__'

# TaskPoints Serializer
class TaskPointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskPoints
        fields = '__all__'
