# views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        특정 조직에 속한 Task만 필터링하여 반환
        """
        organization_id = self.request.query_params.get("organization", None)
        
        if organization_id:
            return Task.objects.filter(organization_id=organization_id)
        
        return Task.objects.all()

class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        content = self.request.query_params.get('content')
        organizer = self.request.query_params.get('organizer')
        goal_id = self.request.query_params.get('id')

        queryset = Goal.objects.all()
        if content:
            queryset = queryset.filter(content__icontains=content)
        if organizer:
            queryset = queryset.filter(organizer__username=organizer)
        if goal_id:
            queryset = queryset.filter(id=goal_id)

        return queryset

class TaskChatViewSet(viewsets.ModelViewSet):
    queryset = TaskChat.objects.all()
    serializer_class = TaskChatSerializer
    permission_classes = [IsAuthenticated]