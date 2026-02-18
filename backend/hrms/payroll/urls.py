from django.urls import path
from . import views

urlpatterns = [
    path('salary-structures/', views.EmployeeSalaryStructureListCreateView.as_view(), name='employee-salary-structure-list-create'),
    path('salary-structures/<int:pk>/', views.EmployeeSalaryStructureDetailView.as_view(), name='employee-salary-structure-detail'),
    path('payrolls/', views.PayrollListCreateView.as_view(), name='payroll-list-create'),
    path('payrolls/<int:pk>/', views.PayrollDetailView.as_view(), name='payroll-detail'),           
    path('payrolls/<int:payroll_id>/components/', views.PayrollSalaryComponentListCreateView.as_view(), name='payroll-salary-component-list-create'),
    path('payrolls/<int:payroll_id>/components/<int:pk>/', views.PayrollSalaryComponentDetailView.as_view(), name='payroll-salary-component-detail'),
    path('payrolls/<int:payroll_id>/advances/', views.PayrollSalaryAdvanceListCreateView.as_view(), name='payroll-salary-advance-list-create'),
    path('payrolls/<int:payroll_id>/advances/<int:pk>/', views.PayrollSalaryAdvanceDetailView.as_view(), name='payroll-salary-advance-detail'),
    path('payrolls/<int:payroll_id>/loans/', views.PayrollSalaryLoanListCreateView.as_view(), name='payroll-salary-loan-list-create'),
    path('payrolls/<int:payroll_id>/loans/<int:pk>/', views.PayrollSalaryLoanDetailView.as_view(), name='payroll-salary-loan-detail'),
]