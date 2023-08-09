from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Errand
from account.models import *

# server

def errand_home(request):
    address_search = request.GET.get('address_search')
    errands = Errand.objects.order_by('-created_at')
    if address_search:
        errands = errands.filter(address_1__icontains=address_search)
    return render(request, 'errand_home.html', {'errands':errands})

@login_required
def errand_detail(request, id):
    errand = get_object_or_404(Errand, pk = id)

    current_user = request.user
    point = current_user.point
    return render(request, 'errand_detail.html', {'errand':errand, 'point':point})

@login_required
def accept_errand(request, id):
    accept_errand = Errand.objects.get(id=id)
    accept_errand.server = request.user
    accept_errand.status = 'in_progress'

    current_point = accept_errand.server.point
    accept_errand.server.point = current_point - 100

    accept_errand.server.save()
    accept_errand.save()
    return redirect('errand_home')

# @login_required
# def ongoing_errand(request):
#     current_user = request.user
#     ongoing_errands = Errand.objects.filter(server=current_user, status='in_progress')
#     return render(request, 'ongoing_errand.html', {'ongoing_errands': ongoing_errands})

def errand_detail_for_server(request, errand_id):
    errand = get_object_or_404(Errand, id=errand_id)
    return render(request, 'errand_detail_for_server.html', {'errand': errand})

def errand_complete(request, errand_id):
    errand = get_object_or_404(Errand, id=errand_id)
    errand.status = 'completed'
    errand.save()
    return redirect('errand_home')

def errand_accept_delete(request, errand_id):
    errand = get_object_or_404(Errand, id=errand_id)
    errand.status = 'pending'
    errand.server = None
    errand.save()
    return redirect('errand_home')

@login_required
def mypage(request):
    user = request.user

    ongoing_errands = Errand.objects.filter(server=user, status='in_progress').order_by('-created_at')
    past_errands = Errand.objects.filter(server=user, status='completed').order_by('-created_at')
    return render(request, 'mypage.html', {'user': user, 'ongoing_errands': ongoing_errands, 'past_errands': past_errands})

# @login_required
# def server_errand_list(request):
#     current_user = request.user
#     past_errands = Errand.objects.filter(server=current_user)
#     return render(request, 'server_errand_list.html', {'past_errands': past_errands})

# @login_required
# def membership_withdrawal(request):
#     current_user = request.user
#     current_user.delete()
#     return redirect('index')

# client 

@login_required
def errand_new(request):
    return render(request, 'errand_new.html')

@login_required
def errand_create(request):
    new_errand = Errand()
    new_errand.item = request.POST['item']
    new_errand.address_1 = request.POST['address-1']
    new_errand.address_2 = request.POST['address-2']
    new_errand.created_at = timezone.now()
    new_errand.client = request.user
    new_errand.save()
    return redirect('client_home')

def errand_delete(request, id):
    delete_errand = Errand.objects.get(id=id)
    delete_errand.delete()
    return redirect('client_home')

@login_required
def client_home(request):
    current_user = request.user
    requested_errands = Errand.objects.filter(client=current_user).order_by('-created_at')
    return render(request, 'client_home.html', {'requested_errands': requested_errands})

def errand_detail_for_client(request, errand_id):
    client = request.user
    errand = get_object_or_404(Errand, id=errand_id, client=client)
    return render(request, 'errand_detail_for_client.html', {'errand': errand})