from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import mixins
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from registrytotal import settings

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
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()


class InspectionRecordByCenterViewSet(viewsets.ModelViewSet):
    serializer_class = InspectionRecordSerializer
    queryset = InspectionRecord.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = InspectionRecord.objects.filter(
            center_id=request.GET.get("center_id")
        )
        serializer = InspectionRecordSerializer(queryset, many=True)
        return Response(serializer.data)


class UserRegisterView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserLoginSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["password"] = make_password(
                serializer.validated_data["password"]
            )
            serializer.save(user_type="1")
            return Response(
                {"message": "User created successfully"}, status=status.HTTP_201_CREATED
            )
        return Response(
            {"message": "Email exists", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )
