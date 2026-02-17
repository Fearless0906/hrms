from django.contrib import admin
from .models import Department, Designation, Branch, Employee, EmployeeDocument, EmployeeEducation, EmployeeExperience, EmployeeSkill

# Register your models here.
admin.site.register(Department)
admin.site.register(Designation)
admin.site.register(Branch)
admin.site.register(Employee)
admin.site.register(EmployeeDocument)
admin.site.register(EmployeeEducation)
admin.site.register(EmployeeExperience)
admin.site.register(EmployeeSkill)