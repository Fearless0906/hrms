from django.urls import path, include

urlpatterns = [
    path('accounts/', include('users.urls')),
    path('department/', include('organization.urls')),
    path('leaves/', include('leaves.urls')),
    path('attendance/', include('attendance.urls')), 
    path('payroll/', include('payroll.urls')),
    path('recruitment/', include('recruitment.urls')),
    path('training/', include('training.urls')),
    path('performance/', include('performance.urls')),
    path('communication/', include('communication.urls')),
]