from rest_framework import viewsets
from rest_framework.response import Response

from .models import *
from .serializers import *
# Create your views here.

class InspectionViewSet(viewsets.ModelViewSet):
    serializer_class = InspectionSerializer
    queryset = Inspection.objects.all()

class InspectionCenterViewSet(viewsets.ModelViewSet):
    serializer_class = InspectionCenterSerializer
    queryset = InspectionCenter.objects.all()
    
class InspectionRecordViewSet(viewsets.ModelViewSet):
    serializer_class = InspectionRecordSerializer
    queryset = InspectionRecord.objects.all()
    
class OwnerViewSet(viewsets.ModelViewSet):
    serializer_class = OwnerSerializer
    queryset = Owner.objects.all()
    
class UploadViewSet(viewsets.ModelViewSet):
    serializer_class = UploadSerializer
    queryset = Upload.objects.all()
    
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    
class InspectionRecordByCenterViewSet(viewsets.ModelViewSet):
    serializer_class = InspectionRecordSerializer
    queryset = InspectionRecord.objects.all()
    
    def list(self, request, *args, **kwargs):
        queryset = InspectionRecord.objects.filter(center_id=request.GET.get('center_id'))
        serializer = InspectionRecordSerializer(queryset, many=True)
        return Response(serializer.data)    