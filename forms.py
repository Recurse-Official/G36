from django import forms
from django.contrib.auth.models import User
from .models import Appointment,VetProfile,supplier,products
class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields=['owner','name','age','species','breed','vet_name','date','status']
class signupForm(forms.Modelform):
    password=forms.Charfield(widget=forms.PasswordInput,label='Password')
    class Meta:
        model=User
        fields=['username','email','password']
class VetForm(forms.Modelform):
    class Meta:
        model=VetProfile
        fields=['full_name','speciality','medical_degree']
class supplierForm(forms.ModelForm):
    class Meta:
        model=supplier
        fields=['supplier_name','email','contact_number','address']
class productsForm(forms.ModelForm):
    class Meta:
        model=products
        fields=['supplier','name','description','cost','quantity']


