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
