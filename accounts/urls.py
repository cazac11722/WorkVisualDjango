from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:user_id>/', UserDetailView.as_view(), name='user_detail'),
    path('users/<int:user_id>/delete/', UserDeleteView.as_view(), name='user_delete'),  # 회원 삭제
    path('users/<int:user_id>/update/', UserUpdateView.as_view(), name='user_update'),  # 회원 정보 수정
]
