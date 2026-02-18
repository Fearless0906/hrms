from django.shortcuts import render
from rest_framework import generics, status
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import LeaveType, LeaveRequest, LeaveBalance, Holiday
from .serializers import LeaveTypeSerializer, LeaveRequestSerializer, LeaveBalanceSerializer, HolidaySerializer


# Create your views here.
class LeaveTypeListCreateView(generics.ListCreateAPIView):
    queryset = LeaveType.objects.all()
    serializer_class = LeaveTypeSerializer
    # permission_classes = [IsAuthenticated]
    
class LeaveTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LeaveType.objects.all()
    serializer_class = LeaveTypeSerializer
    # permission_classes = [IsAuthenticated]
    
class LeaveRequestListCreateView(generics.ListCreateAPIView):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer
    # permission_classes = [IsAuthenticated]
    
class LeaveRequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer
    # permission_classes = [IsAuthenticated]
    
class LeaveBalanceListCreateView(generics.ListCreateAPIView):
    queryset = LeaveBalance.objects.all()
    serializer_class = LeaveBalanceSerializer
    # permission_classes = [IsAuthenticated]

class LeaveBalanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LeaveBalance.objects.all()
    serializer_class = LeaveBalanceSerializer
    # permission_classes = [IsAuthenticated]
    
class HolidayListCreateView(generics.ListCreateAPIView):
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer
    # permission_classes = [IsAuthenticated]
    
class HolidayDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer
    # permission_classes = [IsAuthenticated]
    
    