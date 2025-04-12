import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestDevicesListAPI:

    def test_GET_devices_list_status_200(self):
        client = APIClient()
        url = reverse("devices:list")
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
