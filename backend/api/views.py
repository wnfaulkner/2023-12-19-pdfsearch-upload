# API VIEWS

import os
import sys
import django
from django.shortcuts import render
from django.http import JsonResponse
# from django.views.decorators import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
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

# Views

@api_view(['GET'])
def file_list(request):
	print("FILES VIEW GET CALLED!")
	try:
		files = File.objects.all().order_by('id')
		serializer = FileSerializer(files, many=True)
		return JsonResponse(serializer.data, safe=False)
	except:
		return 'Error in files_view GET'

@api_view(['POST'])
def file_upload(request):
    print("FILES VIEW POST CALLED!", request)#, request.FILES)
    parsed_data = JSONParser().parse(request.FILES)
    serializer = FileSerializer(data=parsed_data)
    if serializer.is_valid():
        # file_obj = File.objects.create(pdf=request.FILES)
        # file_obj.pdf_text = extract_text(file_obj)
        serializer.save()
        # return JsonResponse({'file_id': file_obj.id}, status=200)
    else:
        return JsonResponse({'error': serializer.errors}, status=400)






		
    # try:
		# 	# print("TRIED!")
		# 	parsed_data = JSONParser().parse(request['FILES'])
		# 	serializer = FileSerializer(data=parsed_data)
		# 	if serializer.is_valid():
		# 			file_obj = File.objects.create(pdf=request.FILES)
		# 			# file_obj.pdf_text = extract_text(file_obj)
		# 			file_obj.save()
		# 			return JsonResponse({'file_id': file_obj.id}, status=200)
		# 	else:
		# 			return JsonResponse({'error': serializer.errors}, status=400)
    # except Exception as e:
    #     return JsonResponse({'error': str(e)}, status=500)

# class FileViewSet(viewsets.ModelViewSet):
# 	queryset = File.objects.all().order_by('id')
# 	serializer_class = FileSerializer
# 	print("FILE VIEW SET CALLED!")













# 	# print("FILES VIEW CALLED!")

# 	if request.method == 'GET':
# 		print("FILES VIEW GET CALLED!")
# 		try:
# 			files = File.objects.all().order_by('id')
# 			serializer = FileSerializer(files, many=True)
# 			return JsonResponse(serializer.data, safe=False)
# 		except:
# 			return 'Error in files_view GET'

# 	if request.method == 'POST':
# 		print("FILES VIEW POST CALLED!", request.FILES)
# 		try:
# 			serializer = FileSerializer(files = request.FILES)
# 			if serializer.is_valid():
# 				file_obj = File.objects.create(pdf=request.FILES['file'])
# 				file_obj.pdf_text = extract_text(file_obj)
# 				file_obj.save()
# 			return JsonResponse({'file_id': file_obj.id}, status=200)
# 		except:
# 			return 'Error in files_view POST'
		



# def store_pdf_text(request, file_id):
# 	print("EXTRACT TEXT CALLED!")
# 	file_obj = File.objects.get(id=file_id)
# 	file_obj.pdf_text = extract_text(file_obj)
# 	file_obj.save()