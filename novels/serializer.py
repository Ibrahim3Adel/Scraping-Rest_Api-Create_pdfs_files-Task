from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import novel_auth

class novelserializer(serializers.ModelSerializer):
    class Meta:
        model = novel_auth
        fields = '__all__'