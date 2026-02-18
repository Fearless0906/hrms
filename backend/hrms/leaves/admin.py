from django.contrib import admin
from .models import LeaveType, LeaveRequest, LeaveBalance, Holiday

# Register your models here.
admin.site.register(LeaveType)
admin.site.register(LeaveRequest)
admin.site.register(LeaveBalance)
admin.site.register(Holiday)

