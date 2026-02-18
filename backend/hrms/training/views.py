from django.shortcuts import render
from rest_framework import generics, status
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TrainingProgram, EmployeeTrainingEnrollment, TrainingCertification
from .serializers import TrainingProgramSerializer, EmployeeTrainingEnrollmentSerializer, TrainingCertificationSerializer


# Create your views here.
class TrainingProgramListCreateView(generics.ListCreateAPIView):
    queryset = TrainingProgram.objects.all()
    serializer_class = TrainingProgramSerializer
    # permission_classes = [IsAuthenticated]

class TrainingProgramDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrainingProgram.objects.all()
    serializer_class = TrainingProgramSerializer
    # permission_classes = [IsAuthenticated]

class EmployeeTrainingEnrollmentListCreateView(generics.ListCreateAPIView):
    queryset = EmployeeTrainingEnrollment.objects.all()
    serializer_class = EmployeeTrainingEnrollmentSerializer
    # permission_classes = [IsAuthenticated]

class EmployeeTrainingEnrollmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeTrainingEnrollment.objects.all()
    serializer_class = EmployeeTrainingEnrollmentSerializer
    # permission_classes = [IsAuthenticated]

class TrainingCertificationListCreateView(generics.ListCreateAPIView):
    queryset = TrainingCertification.objects.all()
    serializer_class = TrainingCertificationSerializer
    # permission_classes = [IsAuthenticated]

class TrainingCertificationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrainingCertification.objects.all()
    serializer_class = TrainingCertificationSerializer
    # permission_classes = [IsAuthenticated]
