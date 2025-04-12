import pytest 
from devices.tests.fixtrues import authenticated_admin_client, user_client
from django.urls import reverse
from devices.tests.data import DATA
from rest_framework import status
from rest_framework.test import APIClient
from devices.models import Device

@pytest.mark.django_db
class TestDevicesAddAPI:
    
    def test_POST_devices_add_status_201(self,authenticated_admin_client):
        client = authenticated_admin_client
        url = reverse('devices:add')
        response = client.post(url, data=DATA,format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert Device.objects.filter(device_name=DATA['device_name']).exists()

    def test_POST_devices_add_status_403(self,user_client):
        client = user_client
        url = reverse('devices:add')
        response = client.post(url, data=DATA,format='json')
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert not Device.objects.filter(device_name=DATA['device_name']).exists()

    def test_POST_devices_add_status_401(self):
        client = APIClient()
        url = reverse('devices:add')
        response = client.post(url,data=DATA,format='json')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert not Device.objects.filter(device_name=DATA['device_name']).exists()