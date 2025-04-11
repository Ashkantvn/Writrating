from rest_framework.views import APIView
from devices.models import Device
from devices.api.v1 import serializers
from rest_framework import status
from rest_framework.response import Response

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
    pass