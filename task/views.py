from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Task, TaskTimeInfo, TaskPerformance, TaskPoints, ProjectTask
from .serializers import (
    TaskSerializer, TaskTimeInfoSerializer, TaskPerformanceSerializer,
    TaskPointsSerializer, ProjectTaskSerializer
)

# 전체 업무 조회 및 생성
class TaskAPIView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 특정 업무 조회, 수정, 삭제
class TaskDetailAPIView(APIView):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return Response({"message": "Task deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

class UserTasksAPIView(APIView):
    """
    특정 유저의 모든 업무를 조회하는 API
    """
    def get(self, request, user_id):
        user = User.objects.filter(id=user_id).first()
        if not user:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        tasks = Task.objects.filter(created_by=user.id)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 포인트 조회, 수정 및 삭제
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

    def delete(self, request, pk):
        task_points = get_object_or_404(TaskPoints, task_id=pk)
        task_points.delete()
        return Response({"message": "Task points deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

# 시간 정보 테이블 API
class TaskTimeInfoAPIView(APIView):
    def get(self, request, pk, time_info_pk=None):
        """
        GET:
        - If `time_info_pk` is provided, retrieve the specific `TaskTimeInfo`.
        - Otherwise, retrieve the time info for the specified `Task`.
        """
        task = get_object_or_404(Task, pk=pk)

        if time_info_pk:
            time_info = get_object_or_404(TaskTimeInfo, pk=time_info_pk, task=task)
            serializer = TaskTimeInfoSerializer(time_info)
            return Response(serializer.data, status=status.HTTP_200_OK)

        time_infos = TaskTimeInfo.objects.filter(task=task)
        serializer = TaskTimeInfoSerializer(time_infos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        """
        POST:
        Create a new `TaskTimeInfo` for the given `Task`.
        """
        task = get_object_or_404(Task, pk=pk)
        data = request.data.copy()
        data['task'] = task.id

        serializer = TaskTimeInfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, time_info_pk):
        """
        DELETE:
        Delete the specified `TaskTimeInfo` for the given `Task`.
        """
        task = get_object_or_404(Task, pk=pk)
        time_info = get_object_or_404(TaskTimeInfo, pk=time_info_pk, task=task)
        time_info.delete()
        return Response({"message": "TaskTimeInfo deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

# 성과 테이블 API
class TaskPerformanceAPIView(APIView):
    def get(self, request, pk=None):
        """
        Retrieve single or all performance records.
        """
        if pk:
            performance = get_object_or_404(TaskPerformance, pk=pk)
            serializer = TaskPerformanceSerializer(performance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        performances = TaskPerformance.objects.all()
        serializer = TaskPerformanceSerializer(performances, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Add a new performance record.
        """
        serializer = TaskPerformanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a specific performance record.
        """
        performance = get_object_or_404(TaskPerformance, pk=pk)
        performance.delete()
        return Response({"message": "Performance record deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


# ProjectTask 추가, 조회, 수정 및 삭제
class ProjectTaskAPIView(APIView):
    def get(self, request, pk=None, task_pk=None):
        if task_pk:
            project_task = get_object_or_404(ProjectTask, pk=task_pk)
            serializer = ProjectTaskSerializer(project_task)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif pk:
            project_tasks = ProjectTask.objects.filter(task=pk).all()
            serializer = ProjectTaskSerializer(project_tasks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        project_tasks = ProjectTask.objects.all()
        serializer = ProjectTaskSerializer(project_tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk=None):
        request.data['task'] = pk  # Ensure the project ID is set
        serializer = ProjectTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, task_pk=None):
        project_task = get_object_or_404(ProjectTask, pk=task_pk)
        serializer = ProjectTaskSerializer(project_task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, task_pk=None):
        project_task = get_object_or_404(ProjectTask, pk=task_pk)
        project_task.delete()
        return Response({"message": "ProjectTask deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

