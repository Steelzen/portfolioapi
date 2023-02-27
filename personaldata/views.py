from django.shortcuts import render
from .models import AboutMe, Project
from rest_framework import generics
from .serializers import AboutMeSerializer, ProjectSerializer

# for AboutMe
class AboutMeList(generics.ListAPIView):
    # API endpoint that allows Aboutme to be viewed.
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer

class AboutMeDetail(generics.RetrieveAPIView):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer

class AboutMeUpdate(generics.RetrieveUpdateAPIView):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer


# for Project
class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetail(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectCreate(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer       

class ProjectUpdate(generics.RetrieveUpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDelete(generics.RetrieveDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer        


