from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class EmployeeSalaryStructure(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='salary_structures')
    effective_from = models.DateField()
    effective_to = models.DateField(blank=True, null=True)
    ctc = models.DecimalField(max_digits=10, decimal_places=2)
    gross_salary = models.DecimalField(max_digits=10, decimal_places=2)
    net_salary = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.employee.get_full_name()} - {self.effective_from}"

class Payroll(models.Model):
    PAYROLL_STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('processed', 'Processed'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled'),
    ]
    
    PAYMENT_MENTHOD_CHOICES = [
        ('bank_transfer', 'Bank Transfer'),
        ('cash', 'Cash'),
        ('cheque', 'Cheque'),
    ]
    
    
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payrolls')
    pay_period_start = models.DateField()
    pay_period_end = models.DateField()
    payment_date = models.DateField()
    salary_structure = models.ForeignKey(EmployeeSalaryStructure, on_delete=models.SET_NULL, blank=True, null=True, related_name='payrolls')
    gross_salary = models.DecimalField(max_digits=10, decimal_places=2)
    total_earnings = models.DecimalField(max_digits=10, decimal_places=2)
    total_deductions = models.DecimalField(max_digits=10, decimal_places=2)
    net_salary = models.DecimalField(max_digits=10, decimal_places=2)
    day_in_month = models.IntegerField()
    day_present = models.IntegerField()
    day_absent = models.IntegerField()
    day_on_leave = models.DecimalField(max_digits=5, decimal_places=2)  # Can be fractional for half-day leaves
    paid_days = models.IntegerField()
    unpaid_days = models.IntegerField()
    ovetime_hours = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    overtime_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    bonus = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    reimbursement = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    advance_deduction = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    loan_deduction = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=PAYROLL_STATUS_CHOICES, default='draft')
    payment_method = models.CharField(max_length=50, choices=PAYMENT_MENTHOD_CHOICES, blank=True, null=True)
    transcation_id = models.CharField(max_length=100, blank=True, null=True)
    processed_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='processed_payrolls')
    processed_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.employee.get_full_name()} - {self.pay_period_start}"
    
# =======================================================================
# Payroll Salary Component Models
class PayrollSalaryComponent(models.Model):
    COMPONENT_TYPE_CHOICES = [
        ('earning', 'Earning'),
        ('deduction', 'Deduction'),
    ]
    
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    component_type = models.CharField(max_length=20, choices=COMPONENT_TYPE_CHOICES, blank=True, null=True)
    calculation_type = models.CharField(max_length=20, blank=True, null=True)  # 'fixed', 'percentage', 'formula'
    is_taxable = models.BooleanField(default=False)
    is_part_of_gross = models.BooleanField(default=True)
    is_part_of_ctc = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
# =======================================================================
# Payroll Salary Advance Models
class PayrollSalaryAdvance(models.Model):
    ADVANCE_STATUS_CHOICES = [
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('pending', 'Pending'),
    ]
    
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reypayment_months = models.IntegerField()
    monthy_deduction = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=ADVANCE_STATUS_CHOICES, default='pending')
    
    def __str__(self):
        return f"Advance - {self.amount}"
     
# =======================================================================
# Payroll Salary Loan Models
class PayrollSalaryLoan(models.Model):
    LOAN_TYPE_CHOICES = [
        ('personal_loan', 'Personal Loan'),
        ('vehicle_loan', 'Vehicle Loan'),
        ('home_loan', 'Home Loan'),
        ('education_loan', 'Education Loan'),
        ('other', 'Other'),
    ]
    
    LOAN_STATUS_CHOICES = [
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('pending', 'Pending'),
        ('closed', 'Closed'),
        ('completed', 'Completed'),
    ]
    
    loan_type = models.CharField(max_length=100, choices=LOAN_TYPE_CHOICES, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    tenure_months = models.IntegerField()
    montly_emi = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=LOAN_STATUS_CHOICES, default='pending')
    
    def __str__(self):
        return f"Loan - {self.amount}"