from django.contrib import admin
from .models import JobPosting, JobApplication, InterviewSchedule

# Register your models here.
admin.site.register(JobPosting)
admin.site.register(JobApplication)
admin.site.register(InterviewSchedule)