from django.shortcuts import render
from rest_framework import viewsets
from .models import customer, rocket, payload, launch
from .serializers import customerSerializer, rocketSerializer, payloadSerializer, launchSerializer
from .utils import tenant_from_request  
# Create your views here.


class customerViewSet(viewsets.ModelViewSet):
    serializer_class = customerSerializer
    queryset = customer.objects.all()
    
    def get_queryset(self):
        tenant = tenant_from_request(self.request)
        return super().get_queryset().filter(tenant=tenant)
    
class rocketViewSet(viewsets.ModelViewSet):
    serializer_class = rocketSerializer
    queryset = rocket.objects.all()
    
    def get_queryset(self):
        tenant = tenant_from_request(self.request)
        return super().get_queryset().filter(tenant=tenant)
    
    
class payloadViewSet(viewsets.ModelViewSet):
    serializer_class = payloadSerializer
    queryset = payload.objects.all()
    
    def get_queryset(self):
        tenant = tenant_from_request(self.request)
        return super().get_queryset().filter(tenant=tenant)
    
    
class launchViewSet(viewsets.ModelViewSet):
    serializer_class = launchSerializer
    queryset = launch.objects.all()
    
    def get_queryset(self):
        tenant = tenant_from_request(self.request)
        return super().get_queryset().filter(tenant=tenant)