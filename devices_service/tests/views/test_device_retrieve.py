import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from api.models import DeviceRate


@pytest.mark.django_db
class TestDeviceRetrieve:
    def setup_method(self):
        self.client = APIClient()
        self.data = {"rate_number": 8.1}

    def test_POST_device_retrieve_status_201(self, normal_user_client, device):
        url = reverse("api:v1:retrieve", args=[device.device_slug])
        response = normal_user_client.post(url, self.data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data.get("data") == "Device rated successfully."
        rate_created = DeviceRate.objects.filter(
            device=device, rate__rate_number=self.data["rate_number"]
        ).exists()
        assert rate_created, "DeviceRate not created."

    def test_POST_device_retrieve_status_404(self, normal_user_client):
        url = reverse("api:v1:retrieve", args=["device"])
        response = normal_user_client.post(url, self.data)
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data.get("detail") == "Device not found."

    def test_POST_device_retrieve_status_401(self, device):
        url = reverse("api:v1:retrieve", args=[device.device_slug])
        response = self.client.post(url, self.data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_POST_device_retrieve_status_400(self, normal_user_client, device):
        url = reverse("api:v1:retrieve", args=[device.device_slug])
        data = {"rate_number": 986.65}
        response = normal_user_client.post(url, data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        detail = response.data.get("detail")
        error_message = (
            "Value must be between 1.0 and 10.0, Examples: 1, 5.5, 10"
        )
        assert detail == error_message

    def test_GET_device_retrieve_status_200(self, device):
        url = reverse("api:v1:retrieve", args=[device.device_slug])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert "device" in response.data.get("data")

    def test_GET_device_retrieve_status_404(self):
        url = reverse("api:v1:retrieve", args=["device"])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data.get("detail") == "device not found."
