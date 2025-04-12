import pytest 
from devices.tests.fixtrues import authenticated_admin_client, device , user_client
from django.urls import reverse
from rest_framework.test import APIClient
from devices.models import Device

@pytest.mark.django_db
class TestEditDeviceAPI:
    
    def test_PATCH_device_edit_status_200(self, authenticated_admin_client, device):
        client = authenticated_admin_client
        url = reverse('devices:edit', kwargs={'slug': device.slug})
        response = client.patch(url, data={'device_name': 'new device name'},format='json')
        assert response.status_code == 200
        device.refresh_from_db()
        assert device.device_name == 'new device name'

    def test_PATCH_device_edit_status_401(self,device):
        client = APIClient()
        url = reverse('devices:edit', kwargs={'slug': device.slug})
        response = client.patch(url, data={'device_name': 'new device name'},format='json')
        assert response.status_code == 401
        device.refresh_from_db()
        assert not device.device_name == 'new device name'

    def test_PATCH_device_edit_status_403(self,user_client,device):
        client = user_client
        url = reverse('devices:edit', kwargs={'slug': device.slug})
        response = client.patch(url, data={'device_name': 'new device name'},format='json')
        assert response.status_code == 403
        device.refresh_from_db()
        assert not device.device_name == 'new device name'        

    def test_PATCH_device_edit_status_404(self,authenticated_admin_client):
        client = authenticated_admin_client
        url = reverse('devices:edit', kwargs={'slug': 'non-existent-slug'})
        response = client.patch(url, data={'device_name': 'new device name'},format='json')
        assert response.status_code == 404

    

