from django.shortcuts import render

from rest_framework import viewsets  # import 
from .models import customer, rocket, payload, launch
from .serializers import customerSerializer, rocketSerializer, payloadSerializer, launchSerializer
# Create your views here.


class customerViewSet(viewsets.ModelViewSet):
    serializer_class = customerSerializer
    queryset = customer.objects.all()
    
    
class rocketViewSet(viewsets.ModelViewSet):
    serializer_class = rocketSerializer
    queryset = rocket.objects.all()
    
    
class payloadViewSet(viewsets.ModelViewSet):
    serializer_class = payloadSerializer
    queryset = payload.objects.all()
    
    
class launchViewSet(viewsets.ModelViewSet):
    serializer_class = launchSerializer
    queryset = launch.objects.all()