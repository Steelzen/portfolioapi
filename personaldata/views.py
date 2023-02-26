from django.shortcuts import render
from .models import AboutMe
from rest_framework import generics
from .serializers import AboutMeSerializer

# Create your views here.
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
