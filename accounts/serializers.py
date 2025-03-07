from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)  # 비밀번호 확인 필드

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    # 비밀번호 검증
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("비밀번호가 일치하지 않습니다.")
        return data

    # 사용자 생성
    def create(self, validated_data):
        validated_data.pop('password2')  # 비밀번호 확인 필드 제거
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()  # 사용자 이름 필드
    password = serializers.CharField(write_only=True)  # 비밀번호 필드

class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("새로운 비밀번호가 일치하지 않습니다.")
        return data

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)  # ✅ user 수정 불가

    class Meta:
        model = UserProfile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=False, allow_null=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', None)
        user = User.objects.create(**validated_data)
        
        if profile_data:
            UserProfile.objects.get_or_create(user=user, defaults=profile_data)  # ✅ 중복 방지
        return user
    
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        if profile_data:
            profile, created = UserProfile.objects.get_or_create(user=instance)
            for attr, value in profile_data.items():
                setattr(profile, attr, value)
            profile.save()
        return instance

class OrganizationReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationReason
        fields = '__all__'

class OrganizationUserSerializer(serializers.ModelSerializer):
    userData = UserSerializer(source='user', read_only=True)

    class Meta:
        model = OrganizationUser
        fields = ['id', 'joined_date', 'department', 'rank', 'userData', 'organization', 'user', 'reason']

class OrganizationDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationDepartment
        fields = '__all__'

class OrganizationRankSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationRank
        fields = '__all__'

class OrganizationSerializer(serializers.ModelSerializer):
    userList = OrganizationUserSerializer(many=True, read_only=True, source='organizationuser_set')
    rank_list = serializers.SerializerMethodField()  # ✅ Custom Method 추가
    department_list = serializers.SerializerMethodField()  # ✅ Custom Method 추가

    class Meta:
        model = Organization
        fields = ['id', 'name', 'description', 'upload_date', 'org_count', 'owner', 'rank_list', 'department_list', 'userList']

    def get_rank_list(self, obj):
        ranks = OrganizationRank.objects.filter(organization=obj).distinct()  # ✅ 올바른 필터링 적용
        return OrganizationRankSerializer(ranks, many=True).data

    def get_department_list(self, obj):
        departments = OrganizationDepartment.objects.filter(organization=obj).distinct()  # ✅ 올바른 필터링 적용
        return OrganizationDepartmentSerializer(departments, many=True).data

class OrganizationUserPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationUserPoint
        fields = '__all__'

class OrganizationUserReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationUserReason
        fields = '__all__'

class OrganizationProjectScopeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationProjectScope
        fields = '__all__'

class OrganizationProjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationProjectType
        fields = '__all__'

class OrganizationGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationGoal
        fields = '__all__'

class OrganizationCommonTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationCommonText
        fields = '__all__'

class OrganizationWorkResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationWorkResult
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
