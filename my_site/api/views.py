from rest_framework.decorators import api_view
from rest_framework import generics
from .models import ProjectModel
from .serializers import ProjectSerializer
from django.shortcuts import render

class LeadProjectCreate(generics.ListCreateAPIView):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectSerializer