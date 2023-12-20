# API VIEWS

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
# import fitz  # PyMuPDF

from .models import File
from .serializers import FileSerializer

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all().order_by('id')
    serializer_class = FileSerializer

@csrf_exempt
def parse_pdf(request, file_id):
    try:
        file_obj = File.objects.get(id=file_id)
        pdf_path = file_obj.pdf.path

        with fitz.open(pdf_path) as pdf_document:
            text = ""
            for page_num in range(pdf_document.page_count):
                page = pdf_document[page_num]
                text += page.get_text()

            # Update the File object with extracted text
            file_obj.pdf_text = text
            file_obj.save()

            return JsonResponse({'success': True, 'message': 'PDF parsed successfully.'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})
