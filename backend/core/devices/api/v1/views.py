from rest_framework.views import APIView
from devices.models import Device
from devices.api.v1 import serializers
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from core.permissions import IsAuthenticatedAndAdmin, IsValidator


# Devices list
class DevicesListAPIView(APIView):

    def get(self, request):
        devices = Device.objects.filter(publishable=True)
        serializer = serializers.DeviceSerializer(devices, many=True)
        if devices.count() == 0:
            return Response(
                {"data": [], "detail": "No devices found"}, status=status.HTTP_200_OK
            )
        else:
            return Response(serializer.data, status=status.HTTP_200_OK)


# Devices details
class DeviceDetailsAPIView(APIView):

    def get(self, request, slug):
        device = get_object_or_404(Device, slug=slug, publishable=True)
        serializer = serializers.DeviceSerializer(device)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Add new Device
class DevicesAddAPIView(APIView):
    permission_classes = [IsAuthenticatedAndAdmin]

    def post(self, request):
        serializer = serializers.DeviceManagementSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DeviceEditAPIView(APIView):
    permission_classes = [IsAuthenticatedAndAdmin]

    def patch(self, request, slug):
        device = get_object_or_404(Device, slug=slug)

        # Enforce object level permission
        self.check_object_permissions(request=request, obj=device)

        serializer = serializers.DeviceManagementSerializer(
            instance=device, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeviceDeleteAPIView(APIView):
    permission_classes = [IsAuthenticatedAndAdmin]

    def delete(self, request, slug):
        device = get_object_or_404(Device, slug=slug)

        # Enforce object level permission
        self.check_object_permissions(request=request, obj=device)

        device.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DeviceCheckAPIView(APIView):
    permission_classes = [IsValidator]

    def patch(self, request, slug):
        device = get_object_or_404(Device, slug=slug)

        # Enforce object level permission
        self.check_object_permissions(request=request, obj=device)

        serializer = serializers.DeviceCheckSerializer(
            instance=device, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, slug):
        device = get_object_or_404(Device, slug=slug)

        # Enforce object level permission
        self.check_object_permissions(request=request, obj=device)

        serializer = serializers.DeviceResponseSerializer(
            data=request.data, context={"user": request.user}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"data": "response sent to validator"}, status=status.HTTP_201_CREATED
        )
