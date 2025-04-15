import pytest
from reviews import models
from django.contrib.auth import get_user_model
from devices import models as DevicesModel
from rest_framework.test import APIClient

User = get_user_model()

# Device review
@pytest.fixture
def device_review():
    target = DevicesModel.Device.objects.create(
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
    user = User.objects.get_or_create(
        email="test@test.com",
        password="adjfapwo@#123AFDADS",
        is_active=True,
        is_admin=True    
    )[0]
    review = models.DeviceReview.objects.create(
        author= user.profile,
        target = target,
        rating = 5,
        review_text = "Test Review",
        review_title = "Test Review Title",
        status = False,
        buying_worth = "Test Buying Worth",
        published_date = "2022-12-12"
    )
    yield review
    if review.pk:
        review.delete()
        user.delete()
        target.delete()

# Operating system review
@pytest.fixture
def operating_system_review():
    target = DevicesModel.OperatingSystem.objects.create(
        os_name = "Test OS 1",
        os_version = "Test Version",
        kernel = "Test Kernel",
        description = "Test Description",
        publishable = True,
    )
    user = User.objects.get_or_create(
        email="test@test.com",
        password="adjfapwo@#123AFDADS",
        is_active=True,
        is_admin=True    
    )[0]
    review= models.OperatingSystemReview.objects.create(
        author= user.profile,
        target = target,
        rating = 5,
        review_text = "Test Review",
        review_title = "Test Review Title",
        status = False,
        buying_worth = "Test Buying Worth",
        published_date = "2022-12-12"
    )
    yield review
    if review.pk:
        review.delete()
        target.delete()
        user.delete()

# Processor review
@pytest.fixture
def processor_review():
    target = DevicesModel.Processor.objects.create(
        processor_name = "test processor 2",
        processor_technology = "ARM",
        core = "4",
        refresh_rate = 60,
        cache = "4",
        description = "Test Description",
        release_date = "2022-12-12",
        publishable = True,
    )
    user = User.objects.get_or_create(
        email="test@test.com",
        password="adjfapwo@#123AFDADS",
        is_active=True,
        is_admin=True    
    )[0]
    review = models.ProcessorReview.objects.create(
        author= user.profile,
        target = target,
        rating = 5,
        review_text = "Test Review",
        review_title = "Test Review Title",
        status = False,
        buying_worth = "Test Buying Worth",
        published_date = "2022-12-12"
    )
    yield review
    if review.pk:
        review.delete()
        user.delete()
        target.delete()

# Graphic processor review
@pytest.fixture
def graphic_processor_review():
    target = DevicesModel.GraphicProcessor.objects.create(
        graphic_processor_name = "test graphics processor",
        g_ram = 8,
        ram_type = "DDR4",
        release_date = "2022-12-12",
        publishable = True,
    )
    user = User.objects.get_or_create(
        email="test@test.com",
        password="adjfapwo@#123AFDADS",
        is_active=True,
        is_admin=True    
    )[0]
    review = models.GraphicsProcessorReview.objects.create(
        author= user.profile,
        target = target,
        rating = 5,
        review_text = "Test Review",
        review_title = "Test Review Title",
        status = False,
        buying_worth = "Test Buying Worth",
        published_date = "2022-12-12"
    )
    yield review
    if review.pk:
        review.delete()
        user.delete()
        target.delete()

@pytest.fixture
def admin_client():
    user = User.objects.get_or_create(
        email="test@test.com",
        password="adjfapwo@#123AFDADS",
        is_active=True,
        is_admin=True  
    )[0]
    client = APIClient()
    client.force_authenticate(user=user)
    yield client
    if user.pk:
        user.delete()

@pytest.fixture
def authenticated_client():
    user = User.objects.create(
        email="test2342edflkjihj@test.com",
        password="asdoijfopamwv@#$235",
        is_admin=False,
        is_active=True,
    )
    client = APIClient()
    client.force_authenticate(user=user)
    yield client
    if user.pk:
        user.delete()