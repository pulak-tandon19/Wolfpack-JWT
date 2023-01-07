from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
# from .models import User
from rest_framework import serializers 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password']
