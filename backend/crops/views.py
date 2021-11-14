from django.shortcuts import render
from rest_framework import viewsets
from .models import Crop
from .serializers import CropSerializer

# Create your views here.

class CropView(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_clas = CropSerializer