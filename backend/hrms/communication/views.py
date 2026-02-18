from django.shortcuts import render
from rest_framework import generics, status
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Announcement, PolicyDocument
from .serializers import AnnouncementSerializer, PolicyDocumentSerializer


# Create your views here.
class AnnouncementListCreateView(generics.ListCreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    # permission_classes = [IsAuthenticated]
    
class AnnouncementDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    # permission_classes = [IsAuthenticated]
    
class PolicyDocumentListCreateView(generics.ListCreateAPIView):
    queryset = PolicyDocument.objects.all()
    serializer_class = PolicyDocumentSerializer
    # permission_classes = [IsAuthenticated]
    
class PolicyDocumentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PolicyDocument.objects.all()
    serializer_class = PolicyDocumentSerializer
    # permission_classes = [IsAuthenticated]
    
