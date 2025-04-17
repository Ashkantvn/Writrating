import pytest 
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from devices import models as DevicesModel

User = get_user_model()


@pytest.fixture
def authenticated_client():
    user = User.objects.create_user(
        email="test23032948@test.com",
        password="apoifmewo2#$@#$t08",
        is_active=True,
    )

    client = APIClient()

    client.force_authenticate(
        user=user,
    )
    client.force_login(user=user)

    yield client
    if user.pk:
        user.delete()

# First device

@pytest.fixture
def first_device():
    device = DevicesModel.Device.objects.create(
        device_name="Test Device",
        price=100.0,
        release_date="2022-01-01",
        publishable=False,
        physical_information=DevicesModel.DevicePhysicalInformation.objects.create(
            width=10.0,
            height=20.0,
            thickness=5.0,
            ports="USB",
            material="Metal",
            device_color="Red",
        ),
        hardware_information=DevicesModel.DeviceHardwareInformation.objects.create(
            battery="Li-ion",
            memory=12,
            graphic_processor=DevicesModel.GraphicProcessor.objects.create(
                graphic_processor_name="Test Processor 1",
                g_ram=8,
                ram_type="DDR4",
                release_date="2022-01-01",
            ),
            processor=DevicesModel.Processor.objects.create(
                processor_name="Test Processor 1",
                core="4",
                processor_technology="ARM",
                refresh_rate=60,
                cache="4",
                description="Test Description",
                release_date="2022-01-01",
            ),
            camera=DevicesModel.Camera.objects.create(
                description="Test Camera",
                resolution="1080p",
                features="Test Technology",
                software_features="Test Features",
                zoom=10,
            ),
            display=DevicesModel.Display.objects.create(
                size="10",
                resolution="1080p",
                protection="Test Display",
                technology="Test Technology",
                refresh_rate=60,
                brightness=100,
                features="Test Technology",
            ),
            storage="Test Storage",
            sensors="Test Sensors",
        ),
        software_information=DevicesModel.DeviceSoftwareInformation.objects.create(
            os=DevicesModel.OperatingSystem.objects.create(
                os_name="Test OS 1",
                os_version="1.0",
                kernel="Test Kernel",
                description="Test Description",
            ),
            ui="Test UI",
            pre_installed_softwares="Test Apps",
            update_policy="Test Policy",
            customizability="Test Customization",
        ),
        features=DevicesModel.DeviceFeatures.objects.create(
            accessories="Test Accessories",
            security="Test Security",
            warranty_and_support="2022-01-01",
        ),
        category=DevicesModel.DeviceCategory.objects.create(
            category_name="Test Category"
        ),
    )
    yield device
    if device.pk:
        device.delete()


# Second device
@pytest.fixture
def second_device():
    device = DevicesModel.Device.objects.create(
        device_name="Test Device 2",
        price=100.0,
        release_date="2022-01-01",
        publishable=False,
        physical_information=DevicesModel.DevicePhysicalInformation.objects.create(
            width=10.0,
            height=20.0,
            thickness=5.0,
            ports="USB",
            material="Metal",
            device_color="Red",
        ),
        hardware_information=DevicesModel.DeviceHardwareInformation.objects.create(
            battery="Li-ion",
            memory=12,
            graphic_processor=DevicesModel.GraphicProcessor.objects.create(
                graphic_processor_name="Test Processor",
                g_ram=8,
                ram_type="DDR4",
                release_date="2022-01-01",
            ),
            processor=DevicesModel.Processor.objects.create(
                processor_name="Test Processor",
                core="4",
                processor_technology="ARM",
                refresh_rate=60,
                cache="4",
                description="Test Description",
                release_date="2022-01-01",
            ),
            camera=DevicesModel.Camera.objects.create(
                description="Test Camera",
                resolution="1080p",
                features="Test Technology",
                software_features="Test Features",
                zoom=10,
            ),
            display=DevicesModel.Display.objects.create(
                size="10",
                resolution="1080p",
                protection="Test Display",
                technology="Test Technology",
                refresh_rate=60,
                brightness=100,
                features="Test Technology",
            ),
            storage="Test Storage",
            sensors="Test Sensors",
        ),
        software_information=DevicesModel.DeviceSoftwareInformation.objects.create(
            os=DevicesModel.OperatingSystem.objects.create(
                os_name="Test OS",
                os_version="1.0",
                kernel="Test Kernel",
                description="Test Description",
            ),
            ui="Test UI",
            pre_installed_softwares="Test Apps",
            update_policy="Test Policy",
            customizability="Test Customization",
        ),
        features=DevicesModel.DeviceFeatures.objects.create(
            accessories="Test Accessories",
            security="Test Security",
            warranty_and_support="2022-01-01",
        ),
        category=DevicesModel.DeviceCategory.objects.create(
            category_name="Test Category"
        ),
    )
    yield device
    if device.pk:
        device.delete()
