from django.shortcuts import render
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Create your views here.

def index(request):
    return render(request, 'chatbot/index.html')


def index(request):
    return render(request, 'chatbot/index.html')