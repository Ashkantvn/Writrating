from rest_framework.views import APIView
from devices.models import Device
from devices.api.v1 import serializers
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Devices list
class DevicesListAPIView(APIView):
    
    def get(self, request):
        devices = Device.objects.filter(publishable=True)
        serializer = serializers.DeviceSerializer(devices,many=True)
        if devices.count() == 0:
            return Response({"data":[],"detail":"No devices found"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_200_OK)
        
# Devices details
class DeviceDetailsAPIView(APIView):
    
    def get(self, request,slug):
        device = get_object_or_404(Device, slug=slug, publishable=True)
        serializer = serializers.DeviceSerializer(device)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

# Add new Device
class DevicesAddAPIView(APIView):
    pass