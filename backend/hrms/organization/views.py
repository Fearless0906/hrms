from django.shortcuts import render
from rest_framework import generics, status
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Department, Designation, Branch, Employee, EmployeeDocument, EmployeeEducation, EmployeeExperience, EmployeeSkill
from .serializers import DepartmentSerializer, DesignationSerializer, BranchSerializer, EmployeeSerializer, EmployeeDocumentSerializer, EmployeeEducationSerializer, EmployeeExperienceSerializer, EmployeeSkillSerializer

# Create your views here.
# =========================================================================
# Organization Views
class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    # permission_classes = [IsAuthenticated]
    
class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    # permission_classes = [IsAuthenticated]

class DesignationListCreateView(generics.ListCreateAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    # permission_classes = [IsAuthenticated]
    
class DesignationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    # permission_classes = [IsAuthenticated]
    
class BranchListCreateView(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    # permission_classes = [IsAuthenticated]
    
class BranchDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    # permission_classes = [IsAuthenticated]
    
class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # permission_classes = [IsAuthenticated]
    
class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # permission_classes = [IsAuthenticated]
    
class EmployeeDocumentListCreateView(generics.ListCreateAPIView):
    queryset = EmployeeDocument.objects.all()
    serializer_class = EmployeeDocumentSerializer
    # permission_classes = [IsAuthenticated]
    
class EmployeeDocumentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeDocument.objects.all()
    serializer_class = EmployeeDocumentSerializer
    # permission_classes = [IsAuthenticated]

class EmployeeEducationListCreateView(generics.ListCreateAPIView):
    queryset = EmployeeEducation.objects.all()
    serializer_class = EmployeeEducationSerializer
    # permission_classes = [IsAuthenticated]
    
class EmployeeEducationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeEducation.objects.all()
    serializer_class = EmployeeEducationSerializer
    # permission_classes = [IsAuthenticated]

class EmployeeExperienceListCreateView(generics.ListCreateAPIView):
    queryset = EmployeeExperience.objects.all()
    serializer_class = EmployeeExperienceSerializer
    # permission_classes = [IsAuthenticated]
    
class EmployeeExperienceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeExperience.objects.all()
    serializer_class = EmployeeExperienceSerializer
    # permission_classes = [IsAuthenticated]

class EmployeeSkillListCreateView(generics.ListCreateAPIView):
    queryset = EmployeeSkill.objects.all()
    serializer_class = EmployeeSkillSerializer
    # permission_classes = [IsAuthenticated]
    
class EmployeeSkillDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeSkill.objects.all()
    serializer_class = EmployeeSkillSerializer
    # permission_classes = [IsAuthenticated]
    