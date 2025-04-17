from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from devices.models import Device
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from user_interactions.api.v1.serializer import DeviceSerializer

class CompareDevicesAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, slug1, slug2):
        first_device = get_object_or_404(Device, slug=slug1)
        second_device = get_object_or_404(Device, slug=slug2)

        first_device_serializer = DeviceSerializer(first_device)
        second_device_serializer = DeviceSerializer(second_device)

        if first_device_serializer.data == second_device_serializer.data:
            return Response({"detail": "The devices are the same"}, status=status.HTTP_400_BAD_REQUEST)

        data = {
            "first_device": first_device_serializer.data,
            "second_device": second_device_serializer.data
        }

        return Response(data={"data":data}, status=status.HTTP_200_OK)
        