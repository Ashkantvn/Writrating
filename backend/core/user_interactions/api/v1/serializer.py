from rest_framework import serializers
from devices.models import Device


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        exclude = ["slug", "publishable", "created_at", "updated_at","category"]

