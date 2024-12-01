from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    pet_name = models.CharField(max_length=100)
    pet_age = models.PositiveIntegerField()
    pet_type = models.CharField(max_length=100)
    pet_breed = models.CharField(max_length=100, blank=True)
    symptoms=models.TextField()
    appointment_date=models.DateField()
    appointment_time=models.TimeField()
    owner_name = models.ForeignKey(User, on_delete=models.CASCADE)
    owner_phone=models.PositiveIntegerField(max_length=10)
    owner_email=models.EmailField()
    
    

    def _str_(self):
        return f"{self.name} - {self.vet_name}"

'''class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def _str_(self):
        return self.name
'''
class VetProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=100)
    specialist=models.CharField(max_length=1000)
    medical_degree=models.FileField(upload_to='medical_degrees/')
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.full_name
class supplier(models.Model):
    supplier_name=models.CharField(max_length=100)
    email=models.EmailField()
    contact_number=models.CharField(max_length=10,blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.supplier_name
class products(models.Model):
    supplier=models.ForeignKey(supplier, on_delete=models.CASCADE,related_name='products')
    name=models.CharField(max_length=100)
    description=models.TextField()
    cost=models.PositiveIntegerField()
    quantity=models.PositiveIntegerField(max_length=10,decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

    
    
    





