from rest_framework import serializers
from .models import AboutMe, Project

class AboutMeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutMe
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'

