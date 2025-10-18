from rest_framework.views import APIView
from api.models import Device
from django.db.models import Avg
from api.v1.serializers import DeviceListSerializer
from rest_framework.response import Response
from rest_framework import status

class DeviceListView(APIView):
    def get(self, request):
        devices = Device.objects.all()
        devices = devices.annotate(
            average_rating=Avg("devicerate__rate__rate_number")
        )
        serializer = DeviceListSerializer(devices, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)