# API URLS

# from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import FileViewSet, store_pdf_text

api = DefaultRouter()
api.register('files', FileViewSet, basename='files')
api.register('files/<int:file_id>/', store_pdf_text, basename='store-pdf-text')

urlpatterns = [
  path('api/', include(api.urls)),
]
