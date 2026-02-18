from django.contrib import admin
from .models import EmployeeSalaryStructure, Payroll, PayrollSalaryComponent, PayrollSalaryAdvance, PayrollSalaryLoan

# Register your models here.
admin.site.register(EmployeeSalaryStructure)
admin.site.register(Payroll)    
admin.site.register(PayrollSalaryComponent)
admin.site.register(PayrollSalaryAdvance)
admin.site.register(PayrollSalaryLoan)