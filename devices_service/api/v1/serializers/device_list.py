from rest_framework import serializers
from api.models import Device
from django.core.validators import MinValueValidator, MaxValueValidator


class DeviceListSerializer(serializers.ModelSerializer):
    device_name = serializers.CharField()
    average_rating = serializers.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    class Meta:
        model = Device
        fields = ["device_name", "average_rating"]
