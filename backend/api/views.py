# API VIEWS

from django.shortcuts import render
from rest_framework import viewsets

from .models import Files
from .serializers import FilesSerializer

class FilesViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all().order_by('id')
    serializer_class = FilesSerializer




