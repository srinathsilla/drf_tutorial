from django.urls import path

from .views import api_home

urlpatterns = [
    path('',api_home)   #localhost:8001/api
]