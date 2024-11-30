from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100, blank=True)
    age = models.PositiveIntegerField()

    def _str_(self):
        return self.name

class Appointment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    vet_name = models.CharField(max_length=100)
    date = models.DateTimeField()
    status = models.CharField(max_length=20, default='Pending')

    def _str_(self):
        return f"{self.pet.name} - {self.vet_name}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def _str_(self):
        return self.name