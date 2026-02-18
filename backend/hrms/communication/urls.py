from django.urls import path
from . import views

urlpatterns = [
    path('announcements/', views.AnnouncementListCreateView.as_view(), name='announcement-list-create'),
    path('announcements/<int:pk>/', views.AnnouncementDetailView.as_view(), name='announcement-detail'),
    path('policy-documents/', views.PolicyDocumentListCreateView.as_view(), name='policy-document-list-create'),
    path('policy-documents/<int:pk>/', views.PolicyDocumentDetailView.as_view(), name='policy-document-detail'),
]