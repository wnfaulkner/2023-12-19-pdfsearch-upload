# UTIL: EXTRACT TEXT FROM PDFS

import os
import sys
import django
from PyPDF2 import PdfReader

# Add the project directory to the Python path
sys.path.append('home/wnf/code/2023-12-19-pdfsearch-upload/backend')

# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

#Import the File model
from api.models import File

# file_path = "../media/store/pdfs/Clemens_1986_Of_Asteroids_and_Dinosaurs.pdf"
file_id = 1

file_obj = File.objects.get(id=file_id)
print(file_obj)

doc = PdfReader(file_obj.pdf)

for page in doc.pages:
  extracted_text = page.extract_text()
  print(extracted_text)





# import fitz

# doc = fitz.open(file_path)
# print(doc.page_count)
# doc = fitz.open_document(file_path)




#         pdf_path = file_obj.pdf.path

#         with fitz.open(pdf_path) as pdf_document:
#             text = ""
#             for page_num in range(pdf_document.page_count):
#                 page = pdf_document[page_num]
#                 text += page.get_text()

#             # Update the File object with extracted text
#             file_obj.pdf_text = text
#             file_obj.save()


# for page in doc:
#     output = page.get_text("blocks")
    # previous_block_id = 0 # Set a variable to mark the block id
    # for a block in output:
    #     if block[6] == 0: # We only take the text
    #         if previous_block_id != block[5]:
    #             # Compare the block number
    #             print("\n")
    #         print(block[4])

# @csrf_exempt
# def parse_pdf(request, file_id):
#     try:
#         file_obj = File.objects.get(id=file_id)
#         pdf_path = file_obj.pdf.path

#         with fitz.open(pdf_path) as pdf_document:
#             text = ""
#             for page_num in range(pdf_document.page_count):
#                 page = pdf_document[page_num]
#                 text += page.get_text()

#             # Update the File object with extracted text
#             file_obj.pdf_text = text
#             file_obj.save()

#             return JsonResponse({'success': True, 'message': 'PDF parsed successfully.'})
#     except Exception as e:
#         return JsonResponse({'success': False, 'message': str(e)})