# API URLS

# from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import FileViewSet #, parse_pdf

api = DefaultRouter()
api.register('files', FileViewSet, basename='files')
# api.register('parse-pdf/<int:file_id>/', parse_pdf, basename='parse-pdf')

api = DefaultRouter()
api.register('files', FileViewSet, basename='files')

urlpatterns = [
    path('api/', include(api.urls)),
]
