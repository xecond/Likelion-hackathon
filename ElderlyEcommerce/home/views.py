from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, 'index.html')

def inform(request):
    return render(request, 'inform.html')