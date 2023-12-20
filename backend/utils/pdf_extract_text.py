# UTIL: EXTRACT TEXT FROM PDFS

# import os
# import sys
# import django
from PyPDF2 import PdfReader

# Add the project directory to the Python path
# sys.path.append('home/wnf/code/2023-12-19-pdfsearch-upload/backend')

# Set the Django settings module
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
# django.setup()

#Import the File model
# from api.models import File

# file_path = "../media/store/pdfs/Clemens_1986_Of_Asteroids_and_Dinosaurs.pdf"
# file_id = 1

# file_obj = File.objects.get(id=file_id)
# print(file_obj)

def extract_text(file_obj):

	doc = PdfReader(file_obj.pdf)

	extracted_text = ""
	for page in doc.pages:
		extracted_text += page.extract_text()
		
	print(extracted_text)
	return extracted_text
