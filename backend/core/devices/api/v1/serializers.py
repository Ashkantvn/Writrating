from rest_framework import serializers
from devices import models
from django.db import transaction
from django.contrib.auth import get_user_model
import random

User = get_user_model()

# Physical info serializer
class DevicePhysicalInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DevicePhysicalInformation
        fields = '__all__'
        

# Hardware info serializers
class ProcessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Processor
        exclude = ['slug', 'publishable', 'created_at', 'updated_at']


class GraphicProcessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GraphicProcessor
        exclude = ['slug', 'publishable', 'created_at', 'updated_at']



class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Camera
        fields = '__all__'

class DisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Display
        fields = '__all__'


class DeviceHardwareInformationSerializer(serializers.ModelSerializer):
    processor = ProcessorSerializer()
    graphic_processor = GraphicProcessorSerializer()
    camera = CameraSerializer()
    display = DisplaySerializer()
    class Meta:
        model = models.DeviceHardwareInformation
        fields = '__all__'

# Software info serializers
class OperatingSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OperatingSystem
        exclude = ['slug', 'publishable', 'created_at', 'updated_at']

class DeviceSoftwareInformationSerializer(serializers.ModelSerializer):
    os = OperatingSystemSerializer()
    class Meta:
        model = models.DeviceSoftwareInformation
        fields = '__all__'

# Features serializer
class DeviceFeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DeviceFeatures
        fields = '__all__'

# Category serializer
class DeviceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DeviceCategory
        fields = '__all__'

# Main device serializers
class DeviceManagementSerializer(serializers.ModelSerializer):
    physical_information = DevicePhysicalInformationSerializer()
    hardware_information = DeviceHardwareInformationSerializer()
    software_information = DeviceSoftwareInformationSerializer()
    features = DeviceFeaturesSerializer()
    category = DeviceCategorySerializer()
    class Meta:
        model = models.Device
        exclude = ['slug', 'publishable', 'created_at', 'updated_at']


    def create(self, validated_data):
        # Extract the nested data
        physical_information_data = validated_data.pop('physical_information')

        hardware_information_data = validated_data.pop('hardware_information')
        processor= hardware_information_data.pop('processor')
        graphic_processor= hardware_information_data.pop('graphic_processor')
        camera_data = hardware_information_data.pop('camera')
        display_data = hardware_information_data.pop('display')

        software_information_data = validated_data.pop('software_information')
        operating_system = software_information_data.pop('os')

        features_data = validated_data.pop('features')
        category_data = validated_data.pop('category')

        # Deligate the creation of the nested models
        with transaction.atomic():
            # Create the nested instances
            physical_information_instance = models.DevicePhysicalInformation.objects.create(**physical_information_data)
            
            camera_instance = models.Camera.objects.create(**camera_data)
            display_instance = models.Display.objects.create(**display_data)
            graphic_processor_instance = models.GraphicProcessor.objects.get_or_create(graphic_processor_name=graphic_processor['graphic_processor_name'], defaults=graphic_processor)[0]
            processor_instance = models.Processor.objects.get_or_create(processor_name=processor['processor_name'], defaults=processor)[0]
            hardware_information_data['processor'] = processor_instance
            hardware_information_data['camera'] = camera_instance
            hardware_information_data['display'] = display_instance
            hardware_information_data['graphic_processor'] = graphic_processor_instance

            hardware_information_instance = models.DeviceHardwareInformation.objects.create(**hardware_information_data)

            operating_system_instance = models.OperatingSystem.objects.get_or_create(os_name=operating_system['os_name'], defaults=operating_system)[0]
            software_information_data['os'] = operating_system_instance
            software_information_instance = models.DeviceSoftwareInformation.objects.create(**software_information_data)

            features_instance = models.DeviceFeatures.objects.create(**features_data)
            category_instance = models.DeviceCategory.objects.get_or_create(category_name=category_data['category_name'], defaults=category_data)[0]

            # Assign the nested instances to the main instance
            validated_data['physical_information'] = physical_information_instance
            validated_data['hardware_information'] = hardware_information_instance
            validated_data['software_information'] = software_information_instance
            validated_data['features'] = features_instance
            validated_data['category'] = category_instance

            # Create the device instance
            device_instance = models.Device.objects.create(**validated_data)

        return device_instance

class DeviceSerializer(serializers.ModelSerializer):
    physical_information = DevicePhysicalInformationSerializer()
    hardware_information = DeviceHardwareInformationSerializer()
    software_information = DeviceSoftwareInformationSerializer()
    features = DeviceFeaturesSerializer()
    category = DeviceCategorySerializer()
    class Meta:
        model = models.Device
        fields = '__all__'


# Serializers for checked device's response
class DeviceCheckSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Device
        fields = ['publishable']

class DeviceResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DeviceResponse
        fields = ["title", "content"]

    def create(self, validated_data):
        admins = User.objects.filter(is_admin=True)
        target_admin = random.choice(admins)
        response_to = target_admin.profile

        user = self.context.get("user")
        if not response_to or not user:
            raise serializers.ValidationError(
                detail="A valid user profile is required to create a response."
            )

        profile = getattr(user, "profile", None)
        response = models.DeviceResponse.objects.create(
            response_to=response_to, author=profile, **validated_data
        )
        response.save()

        return response
