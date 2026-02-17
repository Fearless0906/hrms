from django.urls import path, include

urlpatterns = [
    path('accounts/', include('users.urls')),
    path('department/', include('organization.urls')),
]