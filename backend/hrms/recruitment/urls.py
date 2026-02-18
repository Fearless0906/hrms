from django.urls import path
from . import views

urlpatterns = [
    path('job-postings/', views.JobPostingListCreateView.as_view(), name='job-posting-list-create'),
    path('job-postings/<int:pk>/', views.JobPostingDetailView.as_view(), name='job-posting-detail'),
    path('job-applications/', views.JobApplicationListCreateView.as_view(), name='job-application-list-create'),
    path('job-applications/<int:pk>/', views.JobApplicationDetailView.as_view(), name='job-application-detail'),
    path('interview-schedules/', views.InterviewScheduleListCreateView.as_view(), name='interview-schedule-list-create'),
    path('interview-schedules/<int:pk>/', views.InterviewScheduleDetailView.as_view(), name='interview-schedule-detail'),
]