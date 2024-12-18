from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminUserOrReadOnly  # permissions.py에서 가져오기
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import TaskCategory, TaskStatus, TaskTitle, TaskContent, TaskEstimatedTime
from .serializers import (
    TaskCategorySerializer,
    TaskStatusSerializer,
    TaskTitleSerializer,
    TaskContentSerializer,
    TaskEstimatedTimeSerializer,
)

# 업무 카테고리 API
class TaskCategoryAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUserOrReadOnly]
    def get(self, request):
        categories = TaskCategory.objects.all()
        serializer = TaskCategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TaskCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 업무 카테고리 수정 및 삭제 API
class TaskCategoryDetailAPIView(APIView):
    def put(self, request, pk):
        category = get_object_or_404(TaskCategory, pk=pk)
        serializer = TaskCategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = get_object_or_404(TaskCategory, pk=pk)
        category.delete()
        return Response({"message": "삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)

# 업무 상태, 제목, 내용, 예상 시간 API는 동일한 구조로 작성
