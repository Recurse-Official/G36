from django import forms
from .models import Pet,Appointment
class PetForm(forms.ModelForm):
    class Meta:
        model=Pet
        fields=['name','species','breed','age']
class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields=['vet_name','date','status']
