from rest_framework import serializers
from .models import AboutMe

class AboutMeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutMe
        fields = ['pk', 'name', 'email', 'phone', 'summary']