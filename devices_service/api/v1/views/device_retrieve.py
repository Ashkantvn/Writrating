from rest_framework.views import APIView
from api.models import Device, Profile
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg
from api.v1.serializers import DeviceSerializer, RateSerializer
from api.models import DeviceRate
from django.core.cache import cache
from drf_spectacular.utils import extend_schema

class DeviceRetrieveView(APIView):
    def get_serializer_class(self):
        if self.request.method == "POST":
            return RateSerializer
        if self.request.method == "GET":
            return DeviceSerializer

    @extend_schema(operation_id='v1_devices_detail')
    def get(self, request, device_slug):
        try:
            device = Device.objects.annotate(
                average_rating=Avg("devicerate__rate__rate_number")
            ).get(device_slug=device_slug)
        except ObjectDoesNotExist:
            return Response(
                data={"detail": "device not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer_class()(device)
        return Response(data={"data": {"device": serializer.data}})

    def post(self, request, device_slug):
        # Ensure the user is authenticated before allowing rating
        if not request.user.is_authenticated:
            return Response(
                data={"detail": "User not authenticated."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        # Get or create a Profile for the current user (based on username)
        profile = Profile.objects.get_or_create(
            username=request.user.username
        )[0]

        # Retrieve the target device, return 404 if it doesn't exist
        try:
            device = Device.objects.get(device_slug=device_slug)
        except ObjectDoesNotExist:
            return Response(
                data={"detail": "Device not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        # Validate incoming rating data;
        # pass profile in context for serializer usage
        serializer = self.get_serializer_class()(
            data=request.data,
            context={"profile": profile}
        )
        if serializer.is_valid():
            cache.delete("device_list")
            # Check if this profile has already rated this device
            device_rate = DeviceRate.objects.filter(
                device=device, rate__profile=profile
            )
            if device_rate.exists():
                # If an old rating exists: keep a reference, save the Rate,
                # update the DeviceRate relation to point to the new Rate,
                # then delete the old Rate object to avoid duplicates.
                old_rate = device_rate.first().rate
                serializer.save()
                device_rate.update(rate=serializer.instance)
                old_rate.delete()
            else:
                # No previous rating: create the Rate and link it to device
                serializer.save()
                DeviceRate.objects.create(
                    device=device,
                    rate=serializer.instance
                )

            # Success response after creating/updating the rating
            return Response(
                data={"data": "Device rated successfully."},
                status=status.HTTP_201_CREATED,
            )

        # Invalid rating value; return a helpful error message
        return Response(
            data={
                "detail":
                "Value must be between 1.0 and 10.0, Examples: 1, 5.5, 10"
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
