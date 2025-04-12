import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from devices.tests.fixtrues import device
from rest_framework import status


@pytest.mark.django_db
class TestDeviceDetailsAPI:

    def test_GET_device_details_status_200(self, device):
        client = APIClient()
        if not device.publishable:
            device.publishable = True
            device.save()
        url = reverse("devices:details", args=[device.slug])
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_GET_device_details_status_404(self):
        client = APIClient()
        url = reverse("devices:details", args=["non-existent-slug"])
        response = client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND
