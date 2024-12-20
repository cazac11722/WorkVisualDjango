from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/task-management/', include('task_management.urls')),
    path('api/task/', include('task.urls')),
]
