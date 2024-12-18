from django.contrib.auth.models import User
from rest_framework import serializers

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


class UserSerializer(serializers.ModelSerializer):
    # 사용자 정보를 반환하는 시리얼라이저
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff']  # 반환할 필드
