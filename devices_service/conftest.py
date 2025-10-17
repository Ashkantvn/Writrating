import pytest
from api.models import Device,Profile,Rate

@pytest.fixture
def device(db):
    device_obj = Device.objects.create(
        device_name="Test"
    )
    rate = Rate.objects.create(
        rate_number=8.65,
        profile=Profile.objects.create(username="profile2")
    )
    device_obj.rates.add(rate)
    yield device_obj
    if device_obj.pk:
        device_obj.delete()

@pytest.fixture
def profile(db):
    profile_obj = Profile.objects.create(
        username="profile"
    )
    yield profile_obj
    if profile_obj.pk:
        profile_obj.delete()

@pytest.fixture
def rate(db):
    rate_obj = Rate.objects.create(
        rate_number=8.65,
        profile=Profile.objects.create(username="profile")
    )
    yield rate_obj
    if rate_obj.pk:
        rate_obj.delete()