from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer

class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    # 사용자 등록 API
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "사용자가 성공적으로 등록되었습니다."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    # 로그인 API
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)

            if user:
                # 사용자에게 토큰 생성 또는 반환
                token, created = Token.objects.get_or_create(user=user)
                return Response({"token": token.key, "user_id": user.id}, status=status.HTTP_200_OK)
            return Response({"error": "잘못된 자격 증명입니다."}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserListView(APIView):
    """
    모든 사용자 정보를 반환하는 API 엔드포인트
    """

    def get(self, request):
        users = User.objects.all()  # 모든 사용자 가져오기
        serializer = UserSerializer(users, many=True)  # 여러 사용자 직렬화
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserDetailView(APIView):
    """
    특정 회원 ID를 기반으로 사용자 정보를 반환하는 API
    """

    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)  # 특정 ID의 사용자 검색
            serializer = UserSerializer(user)   # 사용자 데이터를 직렬화
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "해당 사용자를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

class UserDeleteView(APIView):
    """
    특정 회원 ID를 기반으로 사용자를 삭제하는 API
    """

    def delete(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)  # 특정 ID의 사용자 검색
            user.delete()  # 사용자 삭제
            return Response({"message": "사용자가 성공적으로 삭제되었습니다."}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "해당 사용자를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)


class UserUpdateView(APIView):
    """
    특정 회원 ID를 기반으로 사용자 정보를 수정하는 API
    """

    def put(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)  # 특정 ID의 사용자 검색
            serializer = UserSerializer(user, data=request.data, partial=True)  # 데이터 직렬화
            if serializer.is_valid():
                serializer.save()  # 사용자 정보 업데이트
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"error": "해당 사용자를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

