from django.shortcuts import render
from rest_framework import generics, status
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import JobPosting, JobApplication, InterviewSchedule
from .serializers import JobPostingSerializer, JobApplicationSerializer, InterviewScheduleSerializer


# Create your views here.
class JobPostingListCreateView(generics.ListCreateAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer
    # permission_classes = [IsAuthenticated]
    
class JobPostingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer
    # permission_classes = [IsAuthenticated]

class JobApplicationListCreateView(generics.ListCreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    # permission_classes = [IsAuthenticated]

class JobApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    # permission_classes = [IsAuthenticated]

class InterviewScheduleListCreateView(generics.ListCreateAPIView):
    queryset = InterviewSchedule.objects.all()
    serializer_class = InterviewScheduleSerializer
    # permission_classes = [IsAuthenticated]
    
class InterviewScheduleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InterviewSchedule.objects.all()
    serializer_class = InterviewScheduleSerializer
    # permission_classes = [IsAuthenticated]

