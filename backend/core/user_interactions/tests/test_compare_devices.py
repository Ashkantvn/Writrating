import pytest 
from django.urls import reverse, resolve
from rest_framework import status
from user_interactions.api.v1 import views


@pytest.mark.django_db
class TestCompareDevices:

    def test_compare_devices_is_resolve(self):
        url = reverse("interactions:compare-devices", kwargs={"slug1": "test1", "slug2": "test2"})
        view_class = resolve(url).func.view_class
        assert view_class == views.CompareDevicesAPIView