# API URLS

# from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import FilesViewSet

api = DefaultRouter()
api.register('files', FilesViewSet, basename='files')

urlpatterns = [
    path('api/', include(api.urls)),
]
