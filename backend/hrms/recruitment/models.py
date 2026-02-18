from django.db import models
from django.contrib.auth import get_user_model
from organization.models import Department, Designation, Branch, Employee

User = get_user_model()


# Create your models here.
class JobPosting(models.Model):
    EMPLOYMENT_CHOICES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
        ('temporary', 'Temporary'),
    ]
    
    JOB_STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('closed', 'Closed'),
        ('on_hold', 'On Hold'),
    ]
    
    job_title = models.CharField(max_length=255)
    job_code = models.CharField(max_length=50, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='job_postings')
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE, related_name='job_postings')
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='job_postings')
    number_of_openings = models.IntegerField()
    employment_type = models.CharField(max_length=50)
    job_description = models.TextField()
    min_experience_years = models.IntegerField()
    max_experience_years = models.IntegerField()
    min_salary = models.DecimalField(max_digits=10, decimal_places=2)
    max_salary = models.DecimalField(max_digits=10, decimal_places=2)
    application_deadline = models.DateField()
    status = models.CharField(max_length=20, choices=JOB_STATUS_CHOICES, default='draft')
    
    def __str__(self):
        return self.job_title

    
# ==================================================================
# Job Application Models
class JobApplication(models.Model):
    APPLICATION_STATUS_CHOICES = [
        ('new', 'New'),
        ('screening', 'Screening'),
        ('interview', 'Interview'),
        ('selected', 'Selected'),
        ('rejected', 'Rejected'),
    ]
    
    APPLICATION_SOURCE_CHOICES = [
        ('career_site', 'Career Site'),
        ('job_portal', 'Job Portal'),
        ('referral', 'Referral'),
        ('linkedin', 'LinkedIn'),
        ('other', 'Other'),
    ]

    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    current_location = models.CharField(max_length=100, blank=True, null=True)
    total_experience_years = models.DecimalField(max_digits=5, decimal_places=2)
    current_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    expected_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    notice_period_days = models.IntegerField(blank=True, null=True)
    cover_letter = models.TextField(blank=True, null=True)
    application_status = models.CharField(max_length=20, choices=APPLICATION_STATUS_CHOICES, default='new')
    source = models.CharField(max_length=100, choices=APPLICATION_SOURCE_CHOICES, blank=True, null=True)  # e.g., LinkedIn, Company Website, Referral
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
    
    
# ==================================================================
# Inveriew Schedule Models
class InterviewSchedule(models.Model):

    INTERVIEW_ROUND_CHOICES = [
        ('phone_screening', 'Phone Screening'),
        ('technical_interview', 'Technical Interview'),
        ('hr_interview', 'HR Interview'),
        ('final_interview', 'Final Interview'),
        ('other', 'Other'),
    ]

    INTERVIEW_TYPE_CHOICES = [
        ('in_person', 'In-person'),
        ('video_call', 'Video Call'),
        ('phone_call', 'Phone Call'),
    ]

    INTERVIEW_STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    RATING_CHOICES = [
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    ]

    RESULTS_CHOICES = [
        ('selected', 'Selected'),
        ('rejected', 'Rejected'),
        ('on_hold', 'On Hold'),
    ]

    RESPONSE_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('sent', 'Sent'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('withdrawn', 'Withdrawn'),
    ]

    interview_round = models.CharField(max_length=50,choices=INTERVIEW_ROUND_CHOICES,blank=True,null=True)
    interview_type = models.CharField(max_length=50,choices=INTERVIEW_TYPE_CHOICES,blank=True,null=True)
    scheduled_date = models.DateTimeField()
    time = models.TimeField()
    interviewers = models.ManyToManyField(Employee,blank=True,related_name='interview_schedules')
    interview_status = models.CharField(max_length=20,choices=INTERVIEW_STATUS_CHOICES,default='scheduled')
    rating = models.IntegerField(choices=RATING_CHOICES,blank=True,null=True)
    result = models.CharField(max_length=20,choices=RESULTS_CHOICES,blank=True,null=True)
    offered_salary = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    joining_date = models.DateField(blank=True, null=True)
    response_status = models.CharField(max_length=20,choices=RESPONSE_STATUS_CHOICES,default='pending')

    def __str__(self):
        return f"Interview for {self.job_application.first_name} {self.job_application.last_name} - {self.interview_round}"

