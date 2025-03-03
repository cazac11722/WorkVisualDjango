from rest_framework import status, viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import *
from .serializers import *

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

class PasswordChangeView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = PasswordChangeSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if not check_password(serializer.validated_data['current_password'], user.password):
                return Response({"error": "현재 비밀번호가 올바르지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)
            
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({"message": "비밀번호가 성공적으로 변경되었습니다."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        owner = self.request.query_params.get('owner', None)
        if owner:
            return Organization.objects.filter(owner__id=owner)
        return Organization.objects.all()

class OrganizationDepartmentViewSet(viewsets.ModelViewSet):
    queryset = OrganizationDepartment.objects.all()
    serializer_class = OrganizationDepartmentSerializer
    permission_classes = [IsAuthenticated]

class OrganizationRankViewSet(viewsets.ModelViewSet):
    queryset = OrganizationRank.objects.all()
    serializer_class = OrganizationRankSerializer
    permission_classes = [IsAuthenticated]

class OrganizationUserViewSet(viewsets.ModelViewSet):
    queryset = OrganizationUser.objects.all()
    serializer_class = OrganizationUserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.query_params.get('user', None)
        if user_id:
            return OrganizationUser.objects.filter(user__id=user_id)
        return OrganizationUser.objects.all()

    def perform_create(self, serializer):
        request_data = serializer.validated_data
        organization = request_data.get("organization")

        if not organization:
            raise serializers.ValidationError({"organization": "조직 정보를 제공해야 합니다."})

        org_user = serializer.save()
        user = org_user.user
        profile, created = UserProfile.objects.get_or_create(user=user)

        profile.company_name = org_user.organization.name
        profile.department = org_user.department.title if org_user.department else ''  # 문자열로 저장
        profile.position = org_user.rank.title if org_user.rank else ''  # 문자열로 저장
        profile.save()

    def perform_update(self, serializer):
        request_data = serializer.validated_data
        organization = request_data.get("organization")

        if not organization:
            raise serializers.ValidationError({"organization": "조직 정보를 제공해야 합니다."})
            
        org_user = serializer.save()
        user = org_user.user
        profile = UserProfile.objects.filter(user=user).first()
        if profile:
            profile.department = org_user.department.title if org_user.department else ''  # 문자열로 저장
            profile.position = org_user.rank.title if org_user.rank else ''  # 문자열로 저장
            profile.save()

    def update(self, request, *args, **kwargs):
        user_id = self.request.query_params.get('user', None)
        
        if user_id:
            instance = self.get_queryset().filter(user__id=user_id).first()
            if not instance:
                return Response({"error": "해당 사용자가 존재하지 않습니다."}, status=404)
            
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)

        return super().update(request, *args, **kwargs)

    def perform_destroy(self, instance):
        user = instance.user
        profile = UserProfile.objects.filter(user=user).first()
        if profile:
            profile.department = ''
            profile.position = ''
            profile.save()
        instance.delete()

class OrganizationUserPointViewSet(viewsets.ModelViewSet):
    queryset = OrganizationUserPoint.objects.all()
    serializer_class = OrganizationUserPointSerializer
    permission_classes = [IsAuthenticated]

class OrganizationUserReasonViewSet(viewsets.ModelViewSet):
    queryset = OrganizationUserReason.objects.all()
    serializer_class = OrganizationUserReasonSerializer
    permission_classes = [IsAuthenticated]

class OrganizationReasonViewSet(viewsets.ModelViewSet):
    queryset = OrganizationReason.objects.all()
    serializer_class = OrganizationReasonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        organization = self.request.query_params.get('organization', None)
        if organization:
            return OrganizationReason.objects.filter(organization__id=organization)
        return OrganizationReason.objects.all()



class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]
