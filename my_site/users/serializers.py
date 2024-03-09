from rest_framework import serializers
from .models import User, ProfileNew

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileNew
        fields = '__all__'
