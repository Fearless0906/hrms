from django.db import models
from django.contrib.auth import get_user_model
from organization.models import Department, Branch


User = get_user_model()

# Create your models here.
class Announcement(models.Model):
    ANNOUNCEMENT_TYPE_CHOICES = [
        ('general', 'General'),
        ('policy', 'Policy'),
        ('event', 'Event'),
        ('urgent', 'Urgent'),
        ('other', 'Other'),
    ]
    
    ANNOUNCEMENT_PRIORITY_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
        ('none', 'None'),
    ]

    
    title = models.CharField(max_length=200)
    content = models.TextField()
    announcement_type = models.CharField(max_length=50, choices=ANNOUNCEMENT_TYPE_CHOICES)
    priority = models.CharField(max_length=50, choices=ANNOUNCEMENT_PRIORITY_CHOICES,)
    target_audience = models.CharField(max_length=100)
    departments = models.ManyToManyField(Department, blank=True)
    branches = models.ManyToManyField(Branch, blank=True)
    published_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class PolicyDocument(models.Model):
    POLICY_CATEGORY_CHOICES = [
        ('all', 'All'),
        ('department', 'Department'),
        ('branch', 'Branch'),
        ('specific', 'Specific'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=POLICY_CATEGORY_CHOICES)
    version = models.CharField(max_length=20)
    effective_from = models.DateField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.title} (v{self.version})"


