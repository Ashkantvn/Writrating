from rest_framework.views import APIView
from api.models import Device
from django.db.models import Avg
from api.v1.serializers import DeviceListSerializer
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache


class DeviceListView(APIView):
    def get(self, request):
        cache_key = "device_list"
        cache_response = cache.get(cache_key)
        if cache_response:
            return Response(data=cache_response, status=status.HTTP_200_OK)
        devices = Device.objects.all()
        devices = devices.annotate(
            average_rating=Avg("devicerate__rate__rate_number")
        )
        serializer = DeviceListSerializer(devices, many=True)
        cache.set(cache_key, {"data": serializer.data}, timeout=60 * 15)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
