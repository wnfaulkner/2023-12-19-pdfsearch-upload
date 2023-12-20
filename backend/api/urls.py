# API URLS

# from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import FileViewSet, parse_pdf

api = DefaultRouter()
# api.register('files', FileViewSet, basename='files')
# api.register('parse-pdf/<int:file_id>/', parse_pdf, basename='parse-pdf')

urlpatterns = [
    path('files', FileViewSet.as_view({ 'get', 'post' }), name='files'),
    path('parse-pdf/<int:file_id>/', parse_pdf, name='parse-pdf')
]
