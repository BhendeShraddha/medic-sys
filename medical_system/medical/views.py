from django.shortcuts import render
from rest_framework import viewsets #Provides built-in CRUD operations for the API.
from .models import Doctor,Patient,Appoinment
from .serializers import DoctorSerializer, PatientSerializer, AppoinmentSerializer

# Create your views here.

# for define Api views for managing Doctors, Patients, and Appointments using Django REST Framework's viewsets.ModelViewSet.
class DoctorViewSet(viewsets.ModelViewSet):
    queryset= Doctor.objects.all()
    serializer_class = DoctorSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset= Patient.objects.all()
    serializer_class = PatientSerializer

class AppoinmentViewSet(viewsets.ModelViewSet):
    queryset = Appoinment.objects.all()
    serializer_class = AppoinmentSerializer