from django.shortcuts import render
from rest_framework import generics, status
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Attendance, AttendancePolicy, AttendanceRegularization
from .serializers import AttendanceSerializer, AttendancePolicySerializer, AttendanceRegularizationSerializer

# Create your views here.

# =========================================================================
# Attendance Views
class AttendanceListCreateView(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    # permission_classes = [IsAuthenticated]
    
class AttendanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    # permission_classes = [IsAuthenticated]
    
class AttendancePolicyListCreateView(generics.ListCreateAPIView):
    queryset = AttendancePolicy.objects.all()
    serializer_class = AttendancePolicySerializer
    # permission_classes = [IsAuthenticated]

class AttendancePolicyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AttendancePolicy.objects.all()
    serializer_class = AttendancePolicySerializer
    # permission_classes = [IsAuthenticated]

class AttendanceRegularizationListCreateView(generics.ListCreateAPIView):
    queryset = AttendanceRegularization.objects.all()
    serializer_class = AttendanceRegularizationSerializer
    # permission_classes = [IsAuthenticated]
    
class AttendanceRegularizationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AttendanceRegularization.objects.all()
    serializer_class = AttendanceRegularizationSerializer
    # permission_classes = [IsAuthenticated]