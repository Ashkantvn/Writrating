from rest_framework.views import APIView
from api.models import Device
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg
from api.v1.serializers import DeviceSerializer

class DeviceRetrieveView(APIView):
    def get(self,request,device_slug):
        try:
            device = Device.objects.annotate(
                average_rating=Avg("devicerate__rate__rate_number")
            ).get(device_slug=device_slug)
        except ObjectDoesNotExist:
            return Response(
                data={
                    "detail":"device not found."
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = DeviceSerializer(device)
        return Response(
            data={
                "data": {
                    "device":serializer.data
                }
            }
        )