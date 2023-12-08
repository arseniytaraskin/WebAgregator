from rest_framework import serializers
from .models import ProjectModel, MainPage

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = '__all__' #все ее поля сериализуем в JSON

class MainPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPage
        fields = '__all__'
