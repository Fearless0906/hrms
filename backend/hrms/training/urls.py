from django.urls import path
from . import views

urlpatterns = [
    path('training-programs/', views.TrainingProgramListCreateView.as_view(), name='training-program-list-create'),
    path('training-programs/<int:pk>/', views.TrainingProgramDetailView.as_view(), name='training-program-detail'),
    path('employee-training-enrollments/', views.EmployeeTrainingEnrollmentListCreateView.as_view(), name='employee-training-enrollment-list-create'),
    path('employee-training-enrollments/<int:pk>/', views.EmployeeTrainingEnrollmentDetailView.as_view(), name='employee-training-enrollment-detail'),
    path('training-certifications/', views.TrainingCertificationListCreateView.as_view(), name='training-certification-list-create'),    
]