from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.

def login(request)
  if request.method == 'GET':
    return render(request, 'login.html')
  if request.method == 'POST'
    userid = request.POST['username']
    userpw = request.POST['password']
    user = auth.autheticate(request, username=userid, password=userpw)
  if user is not None:
    auth.login(request, user)
    return redirect('home')
  else:
    return render(request, 'login.html')

def logout(request)
  auth.logout(request)
  return redirect('home')


def signup(request):
  if request.method == 'GET':
    return render(request, 'signup.html')

  else:
    userid = request.POST['username']
    userpw = request.POST['password']
    new_user = User.objects.create_user(username=userid, password=userpw)
    auth.login(request, new_user)
    return redirect('home')
