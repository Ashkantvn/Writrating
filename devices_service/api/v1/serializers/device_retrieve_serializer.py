from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers
from api.models import Device, Rate

class DeviceSerializer(serializers.ModelSerializer):
    device_name = serializers.CharField()
    average_rating = serializers.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ]
    )

    class Meta:
        model = Device
        fields = ["device_name","average_rating"]

class RateSerializer(serializers.ModelSerializer):
    rate_number = serializers.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ]
    )    

    class Meta:
        model = Rate
        fields = ["rate_number"]

    def create(self, validated_data):
        profile = self.context.get("profile")
        validated_data["profile"] = profile
        return super().create(validated_data)
