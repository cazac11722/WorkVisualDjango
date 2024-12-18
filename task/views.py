from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Task, TaskTimeInfo, TaskPerformance, TaskPoints
from .serializers import TaskSerializer, TaskTimeInfoSerializer, TaskPerformanceSerializer, TaskPointsSerializer

# 전체 업무 조회 및 생성
class TaskAPIView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save(created_by=request.user)
            TaskPoints.objects.create(task=task, points=100)  # 기본 포인트: 100
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 특정 업무 삭제
class TaskDetailAPIView(APIView):
    def delete(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return Response({"message": "Task deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

# 포인트 조회 및 수정
class TaskPointsAPIView(APIView):
    def get(self, request, pk):
        task_points = get_object_or_404(TaskPoints, task_id=pk)
        serializer = TaskPointsSerializer(task_points)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        task_points = get_object_or_404(TaskPoints, task_id=pk)
        serializer = TaskPointsSerializer(task_points, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
