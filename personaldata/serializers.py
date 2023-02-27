from rest_framework import serializers
from .models import AboutMe, Project

class AboutMeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutMe
        fields = ['pk', 'name', 'email', 'phone', 'summary']


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'

