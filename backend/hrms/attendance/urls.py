from django.urls import path
from . import views

urlpatterns = [
    path('attendances/', views.AttendanceListCreateView.as_view(), name='attendance-list-create'),
    path('attendances/<int:pk>/', views.AttendanceDetailView.as_view(), name='attendance-detail'),
    path('attendance-policies/', views.AttendancePolicyListCreateView.as_view(), name='attendance-policy-list-create'), 
    path('attendance-policies/<int:pk>/', views.AttendancePolicyDetailView.as_view(), name='attendance-policy-detail'),
    path('attendance-regularizations/', views.AttendanceRegularizationListCreateView.as_view(), name='attendance-regularization-list-create'),
    path('attendance-regularizations/<int:pk>/', views.AttendanceRegularizationDetailView.as_view(), name='attendance-regularization-detail'),
]