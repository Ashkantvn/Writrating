from rest_framework import serializers
from user_interactions.models import Report
from devices.models import Device

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        exclude = ["slug", "publishable", "created_at", "updated_at","category"]



class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ["report_title","report_content"]
