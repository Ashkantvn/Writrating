from rest_framework.views import APIView
from api.models import Device, Profile
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg
from api.v1.serializers import DeviceSerializer,RateSerializer
from api.models import DeviceRate

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

    def post(self, request, device_slug):
        if not request.user.is_authenticated:
            return Response(
                data={
                    "detail": "User not authenticated."
                },
                status=status.HTTP_401_UNAUTHORIZED
            )
        profile = Profile.objects.get_or_create(
            username=request.user.username
        )[0]
        try:
            device = Device.objects.get(device_slug=device_slug)
        except ObjectDoesNotExist:
            return Response(
                data={
                    "detail": "Device not found."
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = RateSerializer(data=request.data, context={"profile": profile})
        if serializer.is_valid():
            device_rate = DeviceRate.objects.filter(device=device, rate__profile=profile)
            if device_rate.exists():
                old_rate = device_rate.first().rate
                serializer.save()
                device_rate.update(rate=serializer.instance)
                old_rate.delete()
            else:
                serializer.save()
                DeviceRate.objects.create(device=device, rate=serializer.instance)
            return Response(
                data={
                    "data": "Device rated successfully."
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            data={
                "detail":
                    "Value must be between 1.0 and 10.0, Examples: 1, 5.5, 10"

            },
            status=status.HTTP_400_BAD_REQUEST
        )