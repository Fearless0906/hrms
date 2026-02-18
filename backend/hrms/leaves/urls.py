from django.urls import path
from . import views

urlpatterns = [
    path('leave-types/', views.LeaveTypeListCreateView.as_view(), name='leave-type-list-create'),
    path('leave-types/<int:pk>/', views.LeaveTypeDetailView.as_view(), name='leave-type-detail'),
    path('leave-requests/', views.LeaveRequestListCreateView.as_view(), name='leave-request-list-create'),
    path('leave-requests/<int:pk>/', views.LeaveRequestDetailView.as_view(), name='leave-request-detail'),
    path('leave-balances/', views.LeaveBalanceListCreateView.as_view(), name='leave-balance-list-create'),
    path('leave-balances/<int:pk>/', views.LeaveBalanceDetailView.as_view(), name='leave-balance-detail'),
    path('holidays/', views.HolidayListCreateView.as_view(), name='holiday-list-create'),
    path('holidays/<int:pk>/', views.HolidayDetailView.as_view(), name='holiday-detail'),
]