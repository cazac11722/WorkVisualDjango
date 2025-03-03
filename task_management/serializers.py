
# serializers.py
from rest_framework import serializers
from .models import *
from accounts.models import Organization, OrganizationUser
from accounts.serializers import UserProfileSerializer  # accounts 앱에서 가져오기

class TaskSerializer(serializers.ModelSerializer):
    author_profile = UserProfileSerializer(read_only=True, source="author.profile")  # ✅ 작성자의 프로필 정보 추가

    class Meta:
        model = Task
        fields = [
            "id", "title", "upload_date", "modified_date", "progress",
            "attributes", "table_head", "table_body",
            "organization", "author", "author_profile"  # ✅ 작성자 프로필 포함
        ]
        
class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'

class TaskChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskChat
        fields = '__all__'