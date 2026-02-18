from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class TrainingProgram(models.Model):
    TRAINING_CATEGORY_CHOICES = [
        ('technical', 'Technical'),
        ('soft_skills', 'Soft Skills'),
        ('compliance', 'Compliance'),
        ('leadership', 'Leadership'),
        ('other', 'Other'),
    ]
    
    TRAINING_TYPE_CHOICES = [
        ('online', 'Online'),
        ('in_person', 'In-person'),
        ('hybrid', 'Hybrid'),
        ('external', 'External'),
        ('workshop', 'Workshop'),
    ]
    
    TRAINING_STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('on_going', 'Ongoing'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, choices=TRAINING_CATEGORY_CHOICES)
    training_type = models.CharField(max_length=100, choices=TRAINING_TYPE_CHOICES)  # e.g., Online, In-person, Hybrid
    duration_hours = models.DecimalField(max_digits=5, decimal_places=2)
    trainer_name = models.CharField(max_length=100, blank=True, null=True)
    trainer_organization = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    max_participants = models.IntegerField()
    cost_per_participant = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=TRAINING_STATUS_CHOICES, default='scheduled')  # e.g., scheduled, completed, cancelled
    
    def __str__(self):
        return self.title
    
# =======================================================================
# Employee Training Enrollment Models
class EmployeeTrainingEnrollment(models.Model):
    ENROLLMENT_STATUS_CHOICES = [
        ('enrolled', 'Enrolled'),
        ('completed', 'Completed'),
        ('nominated', 'Nominated'),
        ('dropped', 'Dropped'),
    ]
    
    enrollment_status = models.CharField(max_length=20, choices=ENROLLMENT_STATUS_CHOICES, default='enrolled')
    attendance_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    completion_certificate = models.FileField(upload_to='training_certificates/', blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.enrollment_status}"
    
    
# ========================================================================
# Training Certification Models
class TrainingCertification(models.Model):
    certification_name = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    issue_date = models.DateField()
    expiration_date = models.DateField()
    credential_id = models.CharField(max_length=100)
    credential_url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.certification_name