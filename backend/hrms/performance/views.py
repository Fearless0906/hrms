from django.shortcuts import render
from rest_framework import generics, status
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Goal, PerformanceCycle, Feedback, Review
from .serializers import GoalSerializer, PerformanceCycleSerializer, FeedbackSerializer, ReviewSerializer


# Create your views here.
class PerfrmanceCycleListCreateView(generics.ListCreateAPIView):
    queryset = PerformanceCycle.objects.all()
    serializer_class = PerformanceCycleSerializer
    # permission_classes = [IsAuthenticated]
    
class PerformanceCycleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PerformanceCycle.objects.all()
    serializer_class = PerformanceCycleSerializer
    # permission_classes = [IsAuthenticated]
    
class GoalListCreateView(generics.ListCreateAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    # permission_classes = [IsAuthenticated]
    
class GoalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    # permission_classes = [IsAuthenticated]
    
class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = [IsAuthenticated]
    
class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = [IsAuthenticated]
    
class FeedbackListCreateView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    # permission_classes = [IsAuthenticated]
    
class FeedbackDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    # permission_classes = [IsAuthenticated]

