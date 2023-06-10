from rest_framework import serializers
from .models import *

class InspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inspection
        fields = '__all__'

class InspectionCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectionCenter
        fields = '__all__'

class InspectionRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectionRecord
        fields = '__all__'

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'
        
class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

