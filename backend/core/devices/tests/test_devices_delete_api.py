import pytest
from devices.tests.fixtrues import authenticated_admin_client,device, user_client
from django.urls import reverse
from devices.models import Device
from rest_framework import status
from rest_framework.test import APIClient

@pytest.mark.django_db
class TestDeleteDeviceAPI:
    
    def test_DELETE_device_status_204(self, authenticated_admin_client, device):
        client = authenticated_admin_client
        url = reverse('devices:delete', kwargs={'slug': device.slug})
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Device.objects.filter(slug=device.slug).exists()

    def test_DELETE_device_status_401(self,device):
        client = APIClient()
        url = reverse('devices:delete', kwargs={'slug': device.slug})
        response = client.delete(url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert Device.objects.filter(slug=device.slug).exists()

    def test_DELETE_device_status_403(self,user_client,device):
        client = user_client
        url = reverse('devices:delete', kwargs={'slug': device.slug})
        response = client.delete(url)
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert Device.objects.filter(slug=device.slug).exists()
    
    def test_DELETE_device_status_404(self,authenticated_admin_client):
        client = authenticated_admin_client
        url = reverse('devices:delete', kwargs={'slug': 'non-existent-slug'})
        response = client.delete(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    