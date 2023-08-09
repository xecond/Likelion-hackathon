"""
URL configuration for ElderlyEcommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home.views import *
from account.views import *
from errand.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('inform/', inform, name="inform"),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', register_view, name='signup'),
    path('errand-home/', errand_home, name="errand_home"),
    path('errand-home/<int:id>', errand_detail, name="errand_detail"),
    path('errand-home/<int:id>/accept-errand/', accept_errand, name="accept_errand"),
    path('errand-detail-for-server/<int:errand_id>', errand_detail_for_server, name="errand_detail_for_server"),
    path('errand-complete/<int:errand_id>', errand_complete, name="errand_complete"),
    path('errand-accept-delete/<int:errand_id>', errand_accept_delete, name="errand_accept_delete"),
    path('mypage/', mypage, name="mypage"),
    path('errand-new/', errand_new, name="errand_new"),
	path('errand-create/', errand_create, name="errand_create"),
    path('errand-delete/<int:id>', errand_delete, name="errand_delete"),
    path('client-home/', client_home, name="client_home"),
    path('errand-detail-for-client/<int:errand_id>/', errand_detail_for_client, name='errand_detail_for_client'),
]
