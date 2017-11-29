from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    guardian = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, null=True, default=None)
    mobile = models.CharField(max_length=20)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

class Appointment(models.Model):
    date = models.DateField()
    general_comment = models.TextField()
