import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status

@pytest.mark.django_db
class TestDeviceRetrieve:
    def setup_method(self):
        self.client = APIClient()
        self.data = {
            "rate":8.16
        }

    def test_POST_device_retrieve_status_201(self,normal_user_client,device):
        url = reverse("api:v1:retrieve",args=[device.device_slug])
        response = normal_user_client.post(url,self.data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data.get("data") == "Rate created."

    def test_POST_device_retrieve_status_404(self,normal_user_client):
        url = reverse("api:v1:retrieve",args=['device'])
        response = normal_user_client.post(url,self.data)
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data.get("detail") == "Device not found."

    def test_POST_device_retrieve_status_401(self,device):
        url = reverse("api:v1:retrieve",args=[device.device_slug])
        response = self.client.post(url,self.data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_POST_device_retrieve_status_400(self,normal_user_client,device):
        url = reverse("api:v1:retrieve",args=[device.device_slug])
        data={
            "rate":986.65
        }
        response = self.client.post(url,data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        detail = response.data.get("detail")
        assert detail  == "Enter number between 0.0 to 10.0"

    def test_GET_device_retrieve_status_200(self,device):
        url = reverse("api:v1:retrieve",args=[device.device_slug])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert "device" in response.data.get("device")

    def test_GET_device_retrieve_status_404(self):
        url = reverse("api:v1:retrieve",args=["device"])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data.get("detail") == "device not found."
