from .models import *
from rest_framework import serializers

class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'  # This will include all fields from the Employee model