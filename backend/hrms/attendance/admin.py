from django.contrib import admin
from .models import Attendance, AttendancePolicy, AttendanceRegularization

# Register your models here.
admin.site.register(Attendance)
admin.site.register(AttendancePolicy)
admin.site.register(AttendanceRegularization)