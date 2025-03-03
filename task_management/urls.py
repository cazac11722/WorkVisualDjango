# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, GoalViewSet, TaskChatViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'goals', GoalViewSet)
router.register(r'task-chats', TaskChatViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
