from django.shortcuts import render
from rest_framework import generics, status
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import EmployeeSalaryStructure, Payroll, PayrollSalaryComponent, PayrollSalaryAdvance, PayrollSalaryLoan
from .serializers import EmployeeSalaryStructureSerializer, PayrollSerializer, PayrollSalaryComponentSerializer, PayrollSalaryAdvanceSerializer, PayrollSalaryLoanSerializer


# Create your views here.
class EmployeeSalaryStructureListCreateView(generics.ListCreateAPIView):
    queryset = EmployeeSalaryStructure.objects.all()
    serializer_class = EmployeeSalaryStructureSerializer
    # permission_classes = [IsAuthenticated]
    
class EmployeeSalaryStructureDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeSalaryStructure.objects.all()
    serializer_class = EmployeeSalaryStructureSerializer
    # permission_classes = [IsAuthenticated]
    
class PayrollListCreateView(generics.ListCreateAPIView):
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer
    # permission_classes = [IsAuthenticated]

class PayrollDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer
    # permission_classes = [IsAuthenticated]
    
class PayrollSalaryComponentListCreateView(generics.ListCreateAPIView):
    queryset = PayrollSalaryComponent.objects.all()
    serializer_class = PayrollSalaryComponentSerializer
    # permission_classes = [IsAuthenticated]
    
class PayrollSalaryComponentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PayrollSalaryComponent.objects.all()
    serializer_class = PayrollSalaryComponentSerializer
    # permission_classes = [IsAuthenticated]

class PayrollSalaryAdvanceListCreateView(generics.ListCreateAPIView):
    queryset = PayrollSalaryAdvance.objects.all()
    serializer_class = PayrollSalaryAdvanceSerializer
    # permission_classes = [IsAuthenticated]
    
class PayrollSalaryAdvanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PayrollSalaryAdvance.objects.all()
    serializer_class = PayrollSalaryAdvanceSerializer
    # permission_classes = [IsAuthenticated]

class PayrollSalaryLoanListCreateView(generics.ListCreateAPIView):
    queryset = PayrollSalaryLoan.objects.all()
    serializer_class = PayrollSalaryLoanSerializer
    # permission_classes = [IsAuthenticated]
    
class PayrollSalaryLoanDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PayrollSalaryLoan.objects.all()
    serializer_class = PayrollSalaryLoanSerializer
    # permission_classes = [IsAuthenticated]
    
