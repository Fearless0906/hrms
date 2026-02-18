from django.db import models
from django.contrib.auth import get_user_model
from organization.models import Branch

User = get_user_model()

# Create your models here.
class LeaveType(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    default_days_per_year = models.IntegerField()
    max_consecutive_days = models.IntegerField()
    is_paid = models.BooleanField(default=True)
    required_documents = models.BooleanField(default=False)
    carry_forward_allowed = models.BooleanField(default=False)
    max_carry_forward_days = models.IntegerField(default=0)
    color_code = models.CharField(max_length=7, default='#000000')  # For calendar display
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
# =======================================================================
# Leave Balance Models
class LeaveBalance(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leave_balances')
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE, related_name='leave_balances')
    year = models.IntegerField()
    total_allocated = models.DecimalField(max_digits=5, decimal_places=2)
    used = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    pending = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    available = models.DecimalField(max_digits=5, decimal_places=2)
    carried_forward = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    
    class Meta:
        unique_together = ('employee', 'leave_type', 'year')
    
    def __str__(self):
        return f"{self.employee} - {self.leave_type} ({self.year})"
    
# =======================================================================
# Leave Request Models
class LeaveRequest(models.Model):
    HAFT_DAY_SESSION_CHOICES = [
        ('first_half', 'First Half (Morning)'),
        ('second_half', 'Second Half (Afternoon)'),
    ]
    
    LEAVE_REQUEST_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('cancelled', 'Cancelled'),
    ]
    
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leave_requests')
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE, related_name='leave_requests')
    start_date = models.DateField()
    end_date = models.DateField()
    total_days = models.DecimalField(max_digits=5, decimal_places=2)
    is_half_day = models.BooleanField(default=False)
    half_day_session = models.CharField(max_length=20, choices=HAFT_DAY_SESSION_CHOICES, blank=True, null=True)  # 'morning' or 'afternoon'
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=LEAVE_REQUEST_STATUS_CHOICES, default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_leaves')
    approved_at = models.DateTimeField(blank=True, null=True)
    rejected_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='rejected_leaves')
    reject_at = models.DateTimeField(blank=True, null=True)
    rejection_reason = models.TextField(blank=True, null=True)
    cancellation_requested_at = models.DateTimeField(blank=True, null=True)
    supporting_document = models.FileField(upload_to='leave_documents/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.employee} - {self.leave_type} ({self.start_date} to {self.end_date})"
    
# =======================================================================
# Holiday Models
class Holiday(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    is_optional = models.BooleanField(default=False)
    branches = models.ManyToManyField(Branch, blank=True, related_name='holidays')
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name