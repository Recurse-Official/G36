from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100, blank=True)
    vet_name = models.CharField(max_length=100)
    date = models.DateTimeField()
    status = models.CharField(max_length=20, default='Pending')

    def _str_(self):
        return f"{self.name} - {self.vet_name}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def _str_(self):
        return self.name
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

    
    
    





