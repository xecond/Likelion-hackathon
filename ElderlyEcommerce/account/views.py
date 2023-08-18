from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from .forms import RegisterForm
from django.db import IntegrityError

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        try: 
            user = CustomUser.objects.get(name=name, phone_number=phone_number)
            if user is not None:
                login(request, user)
                user_type = request.GET.get('user_type')
                if user_type == 'client':
                    return redirect('client_home')
                elif user_type == 'server':
                    return redirect('errand_home')
                else:
                    return render(request, 'login.html')
        except:
            return render(request, 'login.html', {'error_message': '존재하지 않는 계정입니다. 회원가입을 해주세요.'})

    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def register_view(request):
    if request.method == "POST":
        name = request.POST['name']
        phone_number = request.POST['phone_number']

        try:
            user = CustomUser.objects.create_user(name=name, phone_number=phone_number)
            login(request, user)
        except IntegrityError:
            return render(request, 'signup.html', {'error_message': '이미 존재하는 전화번호입니다.'})
        user_type = request.GET.get('user_type')
        if user_type == 'client':
            return redirect('client_home')
        elif user_type == 'server':
            return redirect('errand_home')
        else:
            return redirect('index')
    return render(request, 'signup.html')
