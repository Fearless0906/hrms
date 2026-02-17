from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee-detail'),
    path('employees/<int:pk>/documents/', views.EmployeeDocumentListCreateView.as_view(), name='employee-document-list-create'),
    path('employees/directory/', views.EmployeeDocumentListCreateView.as_view(), name='employee-directory'),
]