import pytest
from django.urls import reverse, resolve
from api.v1 import views


@pytest.mark.django_db
class TestDeviceAPIUrls:
    def test_device_list_url(self):
        url = reverse("api:v1:list")
        view_class = resolve(url).func.view_class
        assert view_class == views.DeviceListView

    def test_device_retrieve_url(self):
        url = reverse("api:v1:retrieve", kwargs={"device_slug": "test-device"})
        view_class = resolve(url).func.view_class
        assert view_class == views.DeviceRetrieveView
