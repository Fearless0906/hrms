from rest_framework import serializers
from .models import TrainingProgram, EmployeeTrainingEnrollment, TrainingCertification

class TrainingProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingProgram
        fields = '__all__'

class EmployeeTrainingEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeTrainingEnrollment
        fields = '__all__'

class TrainingCertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingCertification
        fields = '__all__'
        
