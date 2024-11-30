"""
URL configuration for petscare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),path('',include('pet.urls')),
]
from django.urls import path
from . import views
urlpatterns=[path('pets/',views.pet_list,name='pet_list'),
             path('pets/add/',views.add_pet,name='add_pet'),
             path('appointments/',views.appointment_list,name='appointment_list'),
             path('appointments/book/', views.book_appointment,name='book_appointment'),
             path('products/',views.product_list,name='product_list')]
