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
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('signup/', signup, name='signup'),
    path('errand-home/', errand_home, name="errand_home"),
    path('errand-home/<int:id>', errand_detail, name="errand_detail"),
    path('errand-new/', errand_new, name="errand_new"),
	path('errand-create/', errand_create, name="errand_create"),
    path('errand-delete/<int:id>', errand_delete, name="errand_delete"),
    path('errand_detail_for_client/<int:errand_id>/', errand_detail_for_client, name='errand_detail_for_client'),
]
