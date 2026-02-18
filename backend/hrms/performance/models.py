from django.db import models
from django.contrib.auth import get_user_model
from organization.models import Employee

User = get_user_model()

# Create your models here.
class PerformanceCycle(models.Model):
    PERFORMANCE_CYCLE_CHOICES = [
        ('quarterly', 'Quarterly'),
        ('half_yearly', 'Half-Yearly'),
        ('annual', 'Annual'),
    ]
    
    name = models.CharField(max_length=100)
    cycle_type = models.CharField(max_length=20)  # e.g., Annual, Semi-Annual, Quarterly
    start_date = models.DateField()
    end_date = models.DateField()
    review_deadline = models.DateField()
    status = models.CharField(max_length=20, choices=PERFORMANCE_CYCLE_CHOICES, default='quanterly') 
    
    def __str__(self):
        return self.name
    
class Goal(models.Model):
    GOAL_STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('abandoned', 'Abandoned'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100)  # e.g., Sales, Customer Service, Product Development
    priority = models.CharField(max_length=20)  # e.g., High, Medium, Low
    target_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=GOAL_STATUS_CHOICES, default='not_started')
    progress_percentage = models.IntegerField(default=0)
    weightage = models.IntegerField(default=0)  # For weighted performance evaluation
    
    def __str__(self):
        return self.title

class Review(models.Model):
    REVIEW_TYPE_CHOICES = [
        ('self', 'Self Review'),
        ('peer', 'Peer Review'),
        ('manager', 'Manager Review'),
        ('subordinate', 'Subordinate Review'),
    ]
    
    REVIEW_STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('acknowledged', 'Acknowledged'),
    ]
    
    reviewer = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='reviews_given')
    review_type = models.CharField(max_length=20, choices=REVIEW_TYPE_CHOICES, default='self')  # e.g., Self, Peer, Manager
    technical_skills_rating = models.IntegerField(blank=True, null=True)
    communication_skills_rating = models.IntegerField(blank=True, null=True)
    teamwork_rating = models.IntegerField(blank=True, null=True)
    leadership_rating = models.IntegerField(blank=True, null=True)
    problem_solving_rating = models.IntegerField(blank=True, null=True)
    punctuality_rating = models.IntegerField(blank=True, null=True)
    overall_rating = models.IntegerField(blank=True, null=True)
    strengths = models.TextField(blank=True, null=True)
    areas_for_improvement = models.TextField(blank=True, null=True)
    achievements = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=REVIEW_STATUS_CHOICES, default='draft')

    def __str__(self):
        return f"{self.reviewer} - {self.review_type}"
    
class Feedback(models.Model):
    FEEDBACK_TYPE_CHOICES = [
        ('positive', 'Positive'),
        ('negative', 'Negative'),
        ('general', 'General'),
        ('constructive', 'Constructive'),
    ]
    
    feedback_type = models.CharField(max_length=100, choices=FEEDBACK_TYPE_CHOICES)
    is_anonymous = models.BooleanField(default=False)
    is_private = models.BooleanField(default=False)
    
    def __str__(self):
        return self.feedback_type