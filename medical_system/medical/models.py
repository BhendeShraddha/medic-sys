from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    
class Patient(models.Model):
    name= models.CharField(max_length=255)
    age= models.IntegerField()
    gender= models.CharField(max_length=10)
    phone= models.CharField(max_length=15)
    email = models.EmailField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Appoinment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name} ({self.date})"