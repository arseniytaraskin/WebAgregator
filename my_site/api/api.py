from .models import ProjectModel
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = ProjectModel.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]

    serializer_class = ProjectSerializer