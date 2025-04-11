import pytest
from django.urls import reverse,resolve
from devices.api.v1 import views




@pytest.mark.django_db
class TestURLS:
    def test_devices_list_url_is_resolved(self):
        url = reverse("devices:list")
        view_class = resolve(url).func.view_class
        assert view_class == views.DevicesListAPIView

    