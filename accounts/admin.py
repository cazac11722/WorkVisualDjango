from django.contrib import admin
from django.contrib.auth.models import User
from .models import *

admin.site.register(UserProfile)
admin.site.register(Organization)
admin.site.register(OrganizationReason)
admin.site.register(OrganizationDepartment)
admin.site.register(OrganizationRank)
admin.site.register(OrganizationUser)
admin.site.register(OrganizationUserPoint)
admin.site.register(OrganizationUserReason)
admin.site.register(Attendance)
