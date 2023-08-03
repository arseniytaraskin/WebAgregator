from rest_framework import serializers
from .models import ProjectModel

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = '__all__' #все ее поля сериализуем в JSON