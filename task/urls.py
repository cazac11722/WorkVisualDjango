from django.urls import path
from .views import TaskAPIView, TaskDetailAPIView, TaskPointsAPIView

urlpatterns = [
    path('tasks/', TaskAPIView.as_view(), name='task_list'),  # 전체 업무 조회 및 생성
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task_detail'),  # 특정 업무 삭제
    path('tasks/<int:pk>/points/', TaskPointsAPIView.as_view(), name='task_points'),  # 포인트 조회 및 수정
]
