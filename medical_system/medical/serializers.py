from rest_framework import serializers
from.models import Doctor,Patient,Appoinment

# without Serializer
# doctors = Doctor.objects.all()
# data = [{"id": doctor.id, "name": doctor.name, "specialty": doctor.specialty} for doctor in doctors]

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

# the Meta class is used to provide metadata about the model being serialized. It defines what model the serializer is associated with and which fields should be included in the API response.

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class AppoinmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appoinment
        fields = '__all__'
