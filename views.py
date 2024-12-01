from django.shortcuts import render,redirect
from .models import Appointment,Product
from .forms import AppointmentForm
def book_appointment(request):
    if request.method=='POST':
        form=AppointmentForm(request.POST)
        if form.is_valid():
            Appointment=form.save(commit=False)
            Appointment.owner=request.user
            Appointment.save()
            return redirect('appointment_list')
        else:
            form=AppointmentForm()
            form.fields['Appointment'].queryset=Appointment.objects.filter(owner=request.user)
            return render(request,'pets/book_appointment.html',{'form':form})
def product_list(request):
    Product=Product.objects.all()
    return render(request,'pets/product_list.html',{'Product':Product})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import signupForm, VetForm
from .models import VetProfile
def signup_view(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = signupForm()
    return render(request, 'signup.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('VetProfile')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')
@login_required
def register_vet(request):
    if request.method == 'POST':
        form = VetForm(request.POST, request.FILES)
        if form.is_valid():
            VetProfile = form.save(commit=False)
            VetProfile.user = request.user
            VetProfile.save()
            return redirect('home')
    else:
        form = VetForm()
    return render(request, 'VetProfile.html', {'form': form})
from django.shortcuts import render, redirect
from .forms import supplierForm, productsForm
from .models import supplier, Product

def add_supplier(request):
    if request.method == 'POST':
        form = supplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
    else:
        form = supplierForm()
    return render(request, 'add_supplier.html', {'form': form})

def add_product(request):
    if request.method == 'POST':
        form = productsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list') 
    else:
        form = productsForm()
    return render(request, 'add_product.html', {'form': form})
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})
    