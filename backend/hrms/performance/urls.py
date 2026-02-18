from django.urls import path
from . import views

urlpatterns = [
    path('goals/', views.GoalListCreateView.as_view(), name='goal-list-create'),
    path('goals/<int:pk>/', views.GoalDetailView.as_view(), name='goal-detail'),
    path('performance-cycles/', views.PerfrmanceCycleListCreateView.as_view(), name='performance-cycle-list-create'),
    path('performance-cycles/<int:pk>/', views.PerformanceCycleDetailView.as_view(), name='performance-cycle-detail'),
    path('feedbacks/', views.FeedbackListCreateView.as_view(), name='feedback-list-create'),
    path('feedbacks/<int:pk>/', views.FeedbackDetailView.as_view(), name='feedback-detail'),
    path('reviews/', views.ReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', views.ReviewDetailView.as_view(), name='review-detail'),
]