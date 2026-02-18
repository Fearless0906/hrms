from rest_framework import serializers
from .models import Attendance, AttendancePolicy, AttendanceRegularization

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
        
class AttendancePolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendancePolicy
        fields = '__all__'
        
class AttendanceRegularizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceRegularization
        fields = '__all__'  

