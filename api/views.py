from rest_framework import viewsets
from rest_framework.response import Response

from .models import *
from .serializers import *
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    
    serializer_class = UserSerializer
    queryset = User.objects.all()
    

    