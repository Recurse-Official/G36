from django.shortcuts import render,redirect
from .models import Pet,Appointment,Product
from .forms import PetForm,AppointmentForm
def pet_list(request):
    pets=Pet.objects.filter(owner=request.user)
    return render(request, 'pets/pet_list.html',{'pets':pets})
def add_pet(request):
    if request.method=='POST':
        form=PetForm(request.POST)
        if form.is_valid():
            pet=form.save(commit=False)
            pet.owner=request.user
            pet.save()
            return redirect ('pet_list')
        else:
            form=PetForm()
            return render(request,'add_pet.html',{'form':form})
def appointment_list(request):
    Appointment=Appointment.objects.filter(pet_owner=request.user)
    return render(request,'pets/appointment.html',{'Appointment':Appointment})
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
            form.fields['pet'].queryset=Pet.objects.filter(owner=request.user)
            return render(request,'pets/book_appointment.html',{'form':form})
def product_list(request):
    Product=Product.objects.all()
    return render(request,'pets/product_list.html',{'Product':Product})

    