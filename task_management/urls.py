from django.urls import path
from .views import TaskCategoryAPIView, TaskCategoryDetailAPIView

urlpatterns = [
    path('categories/', TaskCategoryAPIView.as_view(), name='task_categories'),  # 조회 및 생성
    path('categories/<int:pk>/', TaskCategoryDetailAPIView.as_view(), name='task_category_detail'),  # 수정 및 삭제
]
