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


from rest_framework.response import Response
from rest_framework.decorators import api_view
from medical.models import Doctor
from django.db.models import Max
from django.shortcuts import render

from django.http import HttpResponse
@api_view(['GET'])
def latest_appoinment_api(request):
    doctors = Doctor.objects.annotate(latest_appoinment=Max('appoinment__date'))

    # Log the raw SQL query
    print("📌 Executed SQL Query:", doctors.query)

    data = [{"doctor": doctor.name, "latest_appoinment": doctor.latest_appoinment} for doctor in doctors]
    return Response(data)

def home(request):
    return render(request, 'home.html')


from rest_framework import generics
from .serializers import UserRegisterSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
