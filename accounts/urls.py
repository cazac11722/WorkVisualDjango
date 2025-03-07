from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'users-profile', UserProfileViewSet, basename='users-profile')
router.register(r'organizations', OrganizationViewSet, basename='organizations')
router.register(r'organization-departments', OrganizationDepartmentViewSet, basename='organization-departments')
router.register(r'organization-ranks', OrganizationRankViewSet, basename='organization-ranks')
router.register(r'organization-reasons', OrganizationReasonViewSet, basename='organization-reasons')
router.register(r'organization-users', OrganizationUserViewSet, basename='organization-users')
router.register(r'organization-user-points', OrganizationUserPointViewSet, basename='organization-user-points')
router.register(r'organization-user-reasons', OrganizationUserReasonViewSet, basename='organization-user-reasons')
router.register(r'organization-project-scope', OrganizationProjectScopeViewSet, basename='organization-project-scope')
router.register(r'organization-project-type', OrganizationProjectTypeViewSet, basename='organization-project-type')
router.register(r'organization-goal', OrganizationGoalViewSet, basename='organization-goal')
router.register(r'organization-commontext', OrganizationCommonTextViewSet, basename='organization-commontext')
router.register(r'organization-work-result', OrganizationWorkResultViewSet, basename='organization-work-result')
router.register(r'attendance', AttendanceViewSet, basename='attendance')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('change-password/', PasswordChangeView.as_view(), name='change-password'),

    path('', include(router.urls)),
]
