# API VIEWS

import os
import sys
import django
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
# import fitz  # PyMuPDF

from .models import File
from .serializers import FileSerializer

# Add the project directory to the Python path
sys.path.append('home/wnf/code/2023-12-19-pdfsearch-upload/backend')

# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from utils.pdf_extract_text import extract_text

class FileViewSet(viewsets.ModelViewSet):
	queryset = File.objects.all().order_by('id')
	serializer_class = FileSerializer
	print("FILE VIEW SET CALLED!")

def store_pdf_text(request, file_id):
	print("EXTRACT TEXT CALLED!")
	file_obj = File.objects.get(id=file_id)
	file_obj.pdf_text = extract_text(file_obj)
	file_obj.save()