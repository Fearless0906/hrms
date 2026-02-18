from rest_framework import serializers
from .models import EmployeeSalaryStructure, Payroll, PayrollSalaryComponent, PayrollSalaryAdvance, PayrollSalaryLoan

class EmployeeSalaryStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeSalaryStructure
        fields = '__all__'  
        
class PayrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payroll
        fields = '__all__'  
        
class PayrollSalaryComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayrollSalaryComponent
        fields = '__all__'
        
class PayrollSalaryAdvanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayrollSalaryAdvance
        fields = '__all__'
        
class PayrollSalaryLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayrollSalaryLoan
        fields = '__all__'

