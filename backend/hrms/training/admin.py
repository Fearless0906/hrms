from django.contrib import admin
from .models import TrainingProgram, EmployeeTrainingEnrollment, TrainingCertification


# Register your models here.
admin.site.register(TrainingProgram)
admin.site.register(EmployeeTrainingEnrollment)
admin.site.register(TrainingCertification)