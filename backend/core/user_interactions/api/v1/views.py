from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from devices.models import Device
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from user_interactions.api.v1.serializer import DeviceSerializer, ReportSerializer
from core.permissions import IsValidatorForGET
from user_interactions.models import Report


class CompareDevicesAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, slug1, slug2):
        """
        Compares two devices. Returns a JSON response with both devices if they are not the same.
        Otherwise, returns a 400 response with a message indicating that the devices are the same.
        """
        first_device = get_object_or_404(Device, slug=slug1)
        second_device = get_object_or_404(Device, slug=slug2)

        first_device_serializer = DeviceSerializer(first_device)
        second_device_serializer = DeviceSerializer(second_device)

        if first_device_serializer.data == second_device_serializer.data:
            return Response(
                {"detail": "The devices are the same"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        data = {
            "first_device": first_device_serializer.data,
            "second_device": second_device_serializer.data,
        }

        return Response(data={"data": data}, status=status.HTTP_200_OK)


class ReportingSystemAPIView(APIView):
    permission_classes = [IsAuthenticated, IsValidatorForGET]

    def post(self, request):
        """
        Creates a new report. Returns a 200 response with a message indicating that the report was created.
        """
        serializer = ReportSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "Report created"}, status=status.HTTP_200_OK)

    def get(self, request):
        """
        Returns a list of all reports. Returns a 200 response with the list of reports.
        """
        reports = Report.objects.all()
        serializer = ReportSerializer(reports, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
