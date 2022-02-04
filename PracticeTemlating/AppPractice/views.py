from django.shortcuts import render
from django.urls import path, include
# Create your views here.

def home(request):
    return render(request, 'AppPractice/home.html')

def room(request):
    return render(request, 'AppPractice/room.html')