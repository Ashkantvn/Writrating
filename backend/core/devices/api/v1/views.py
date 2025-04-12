from rest_framework.views import APIView
from devices.models import Device
from devices.api.v1 import serializers
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from core.permissions import IsAuthenticatedAndAdmin

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
    permission_classes = [IsAuthenticatedAndAdmin]
    
    def post(self, request):
        serializer = serializers.DeviceAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DeviceEditAPIView(APIView):
    pass