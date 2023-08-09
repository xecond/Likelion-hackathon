from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from .forms import RegisterForm

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        user = CustomUser.objects.get(phone_number=phone_number)
        if user is not None:
            login(request, user)
            user_type = request.GET.get('user_type')
            if user_type == 'client':
                return redirect('client_home')
            elif user_type == 'server':
                return redirect('errand_home')
            else:
                return render(request, 'login.html')
        else:
            return redirect('index')
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def register_view(request):
    if request.method == "POST":
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        user = CustomUser.objects.create_user(name=name, phone_number=phone_number)

        login(request, user)

        user_type = request.GET.get('user_type')
        if user_type == 'client':
            return redirect('client_home')
        elif user_type == 'server':
            return redirect('errand_home')
        else:
            return redirect('index')
    return render(request, 'signup.html')
