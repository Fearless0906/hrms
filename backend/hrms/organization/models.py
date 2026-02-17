from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
# =========================================================================
# Organization Models
class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, null=True)
    parent_department = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='sub_departments')
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='managed_departments')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
# ========================================================================
# Designation Models
class Designation(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='designations')
    level = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

# =======================================================================
# Branch Models
class Branch(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    is_head_office = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    

# =======================================================================
# Employee Models
class Employee(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    
    MARTIAL_STATUS_CHOICES = [
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed'),
    ]
    
    EMPLOYEE_TYPE_CHOICES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
        ('intern', 'Intern'),
    ]
    
    EMPLOYMENT_STATUS_CHOICES = [
        ('active', 'Active'),
        ('probation', 'Probation'),
        ('resigned', 'Resigned'),
        ('terminated', 'Terminated'),
    ]
    

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True, related_name='employees')
    designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, blank=True, null=True, related_name='employees')
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, blank=True, null=True, related_name='employees')
    reporting_manager = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='subordinates')
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    martial_status = models.CharField(max_length=20, choices=MARTIAL_STATUS_CHOICES, blank=True, null=True)
    blood_group = models.CharField(max_length=5, blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    personal_email = models.EmailField(blank=True, null=True)
    personal_phone = models.CharField(max_length=20, blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact_phone = models.CharField(max_length=20, blank=True, null=True)
    emergency_contact_relationship = models.CharField(max_length=50, blank=True, null=True)
    current_address = models.TextField(blank=True, null=True)
    permanent_address = models.TextField(blank=True, null=True)
    employee_type = models.CharField(max_length=20, choices=EMPLOYEE_TYPE_CHOICES, blank=True, null=True)
    employment_status = models.CharField(max_length=20, choices=EMPLOYMENT_STATUS_CHOICES, blank=True, null=True)
    date_of_joining = models.DateField(blank=True, null=True)
    date_of_confirmation = models.DateField(blank=True, null=True)
    date_of_resignation = models.DateField(blank=True, null=True)
    probation_period_months = models.IntegerField(blank=True, null=True)
    notice_period_days = models.IntegerField(blank=True, null=True) 
    current_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    salary_currency = models.CharField(max_length=10, blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    account_number = models.CharField(max_length=50, blank=True, null=True)
    bank_ifsc_code = models.CharField(max_length=20, blank=True, null=True)
    pan_number = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.employee_id})"
    
# =======================================================================
# Employee Document Models
class EmployeeDocument(models.Model):
    DOCUMENT_TYPE_CHOICES = [
        ('resume', 'Resume'),
        ('cv', 'CV'),
        ('offer_letter', 'Offer Letter'),
        ('id_proof', 'ID Proof'),
        ('education_certificate', 'Education Certificate'),
        ('training_certificate', 'Training Certificate'),
        ('other', 'Other'),
    ]
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='documents')
    document_type = models.CharField(max_length=100, choices=DOCUMENT_TYPE_CHOICES, blank=True, null=True)
    document_name = models.CharField(max_length=255)
    document_file = models.FileField(upload_to='employee_documents/')
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='uploaded_documents')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    verified_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='verified_documents')
    verified_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.document_name} - {self.employee.user.first_name} {self.employee.user.last_name}"
    
# =======================================================================
# Employee Education Models
class EmployeeEducation(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='education')
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=255)
    university = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    grade = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return f"{self.degree} - {self.employee.user.first_name} {self.employee.user.last_name}"
    
# =======================================================================
# Employee Experience Models
class EmployeeExperience(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='experience')
    company_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=100)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.job_title} at {self.company_name} - {self.employee.user.first_name} {self.employee.user.last_name}" 

# =======================================================================
# Employee Skill Models
class EmployeeSkill(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='skills')
    skill_name = models.CharField(max_length=100)
    proficiency_level = models.CharField(max_length=50, blank=True, null=True)
    years_of_experience = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.skill_name} - {self.employee.user.first_name} {self.employee.user.last_name}"