from django.shortcuts import render
from rest_framework import viewsets
from .models import customer, rocket, payload, launch
from .serializers import customerSerializer, rocketSerializer, payloadSerializer, launchSerializer
from .utils import tenant_from_request  
from django.db.models import Q
# Create your views here.


class customerViewSet(viewsets.ModelViewSet):
    serializer_class = customerSerializer
    queryset = customer.objects.all()
    
    def perform_create(self, serializer):
        tenant = tenant_from_request(self.request)
        serializer.save(tenant=tenant)
    
    def get_queryset(self):
        tenant = tenant_from_request(self.request)
        queryset = super().get_queryset()
        
        if tenant is None:
            # If tenant is None, filter objects with null tenant field
            queryset = queryset.filter(Q(tenant__isnull=True))
        else:
            queryset = queryset.filter(tenant=tenant)
            
        return queryset
    
    
class rocketViewSet(viewsets.ModelViewSet):
    serializer_class = rocketSerializer
    queryset = rocket.objects.all()
    
    def perform_create(self, serializer):
        tenant = tenant_from_request(self.request)
        serializer.save(tenant=tenant)
    
    def get_queryset(self):
        tenant = tenant_from_request(self.request)
        queryset = super().get_queryset()
        
        if tenant is None:
            # If tenant is None, filter objects with null tenant field
            queryset = queryset.filter(Q(tenant__isnull=True))
        else:
            queryset = queryset.filter(tenant=tenant)
            
        return queryset
    
    
class payloadViewSet(viewsets.ModelViewSet):
    serializer_class = payloadSerializer
    queryset = payload.objects.all()
    
    def perform_create(self, serializer):
        tenant = tenant_from_request(self.request)
        serializer.save(tenant=tenant)
    
    def get_queryset(self):
        tenant = tenant_from_request(self.request)
        queryset = super().get_queryset()
        
        if tenant is None:
            # If tenant is None, filter objects with null tenant field
            queryset = queryset.filter(Q(tenant__isnull=True))
        else:
            queryset = queryset.filter(tenant=tenant)
            
        return queryset
    
    
class launchViewSet(viewsets.ModelViewSet):
    serializer_class = launchSerializer
    queryset = launch.objects.all()
    
    def perform_create(self, serializer):
        tenant = tenant_from_request(self.request)
        serializer.save(tenant=tenant)
    
    def get_queryset(self):
        tenant = tenant_from_request(self.request)
        queryset = super().get_queryset()
        
        if tenant is None:
            # If tenant is None, filter objects with null tenant field
            queryset = queryset.filter(Q(tenant__isnull=True))
        else:
            queryset = queryset.filter(tenant=tenant)
            
        return queryset