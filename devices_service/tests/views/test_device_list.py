import pytest
from rest_framework import test, status
from django.urls import reverse

@pytest.mark.django_db
class TestDeviceListView:
    def setup_method(self):
        self.url = reverse("api:v1:list")
        self.client = test.APIClient()

    def test_GET_device_list_status_200(self):
        response = self.client.get(self.url)
        assert response.status_code == status.HTTP_200_OK
        assert "data" in response.data