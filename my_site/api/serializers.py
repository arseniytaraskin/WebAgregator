from rest_framework import serializers
from .models import ProjectModel, MainPage, TestModel

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = '__all__' #все ее поля сериализуем в JSON

class TestProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = '__all__'

class MainPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPage
        fields = '__all__'

class MainPageSerializerNew(serializers.ModelSerializer):
    class Meta:
        model = MainPage
        fields = '__all__'
