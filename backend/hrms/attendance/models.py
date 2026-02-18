from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
# ========================================================================
# Attendance Models
class Attendance(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()
    check_in_time = models.TimeField()
    check_out_time = models.TimeField(null=True, blank=True)
    check_in_location = models.CharField(max_length=255, null=True, blank=True)
    check_out_location = models.CharField(max_length=255, null=True, blank=True)
    working_hours = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    overtime_hours = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, default='present')  # present,
    is_late = models.BooleanField(default=False)
    late_by_minutes = models.IntegerField(default=0)
    remarks = models.TextField(blank=True, null=True)
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_attendances')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employee} - {self.date}"
    
# =======================================================================
# Attendance Policy Models
class AttendancePolicy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    working_hours_per_day = models.DecimalField(max_digits=5, decimal_places=2)
    working_days_per_week = models.IntegerField()
    check_in_time = models.TimeField()
    check_out_time = models.TimeField()
    grade_period_minutes = models.IntegerField(default=15)  # Grace period for late check-in
    half_day_threshold_hours = models.DecimalField(max_digits=5, decimal_places=2, default=4.0)  # Threshold for half-day status
    overtime_applicable = models.BooleanField(default=False)
    is_default = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
# =======================================================================
# Attendance Regularization Models
class AttendanceRegularization(models.Model):
    ATTENDACE_REGULARIZATION_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='regularizations')
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE, related_name='regularizations')
    request_check_in = models.DateTimeField(null=True, blank=True)
    request_check_out = models.DateTimeField(null=True, blank=True)
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=ATTENDACE_REGULARIZATION_STATUS_CHOICES, default='pending')
    reviewed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviewed_regularizations')
    reviewed_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.employee} - {self.attendance}"

