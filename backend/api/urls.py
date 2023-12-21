# API URLS

# from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import file_list, file_upload #FileViewSet #, store_pdf_text

# api = DefaultRouter()
# api.register('files', FileViewSet, basename='files')

urlpatterns = [
  # path('api/', include(api.urls)),
  path('api/files/', file_list, name='files-index'),
  path('api/files/upload/', file_upload, name='files-upload'),
]
