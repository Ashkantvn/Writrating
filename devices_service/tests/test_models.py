import pytest
from api.models import DeviceRate,Profile

@pytest.mark.django_db
class TestAPIModels:
    def test_devices_model_is_created(self,device):
        assert device.device_name == "Test"
        rate_added = device.rates.first()
        assert rate_added is not None,"Rate should be added to the device"
        assert device.created_at is not None,"Created date should not be None"
        assert device.updated_at is not None,"Updated date should not be None"

    def test_device_model_str(self,device):
        assert str(device) == device.device_name

    def test_profile_model_is_created(self,profile):
        assert profile.username == "profile"
        assert profile.created_at is not None,"Created date should not be None"
        assert profile.updated_at is not None,"Updated date should not be None"

    def test_profile_model_str(self,profile):
        assert str(profile) == profile.username

    def test_rate_model_is_created(self,rate):
        assert rate.rate_number == 8.65
        is_profile = isinstance(rate.profile,Profile)
        assert is_profile,"rate.profile is not a Profile instance"
        assert rate.created_at is not None,"Created date should not be None"
        assert rate.updated_at is not None,"Updated date should not be None"

    def test_profile_model_str(self,profile):
        assert str(profile) == profile.username