from django.urls import path
from .views import (
    TaskAPIView, TaskDetailAPIView, TaskPointsAPIView,
    ProjectTaskAPIView, TaskTimeInfoAPIView, TaskPerformanceAPIView, UserTasksAPIView
)

urlpatterns = [
    path('', TaskAPIView.as_view(), name='task-list'),
    path('<int:pk>/', TaskDetailAPIView.as_view(), name='task-detail'),

    path('<int:pk>/points/', TaskPointsAPIView.as_view(), name='task-points'),

     # Task Time Info API
    path('<int:pk>/task-time-info/', TaskTimeInfoAPIView.as_view(), name='task-time-info-list-create'),
    path('<int:pk>/task-time-info/<int:time_info_pk>/', TaskTimeInfoAPIView.as_view(), name='task-time-info-detail'),

    # Task Performance API
    path('task-performance/', TaskPerformanceAPIView.as_view(), name='task-performance-list-create'),
    path('task-performance/<int:pk>/', TaskPerformanceAPIView.as_view(), name='task-performance-detail'),

    path('<int:pk>/project-tasks/', ProjectTaskAPIView.as_view(), name='project-task-list-create'),
    path('<int:pk>/project-tasks/<int:task_pk>/', ProjectTaskAPIView.as_view(), name='project-task-detail'),

    # 특정 유저 업무 전체 조회
     path('user/<int:user_id>/tasks/', UserTasksAPIView.as_view(), name='user-tasks'),
]
