from .models import customer, rocket, payload, launch
from rest_framework import serializers

class customerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = customer
        exclude = ('tenant',)
        
class rocketSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = rocket
        exclude = ('tenant',)
        
class payloadSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = payload
        exclude = ('tenant',)
        
class launchSerializer(serializers.HyperlinkedModelSerializer):
    
    rockets = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = launch
        exclude = ('tenant',)