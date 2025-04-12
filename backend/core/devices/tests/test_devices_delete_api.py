import pytest
from devices.tests.fixtrues import authenticated_admin_client,device
from django.urls import reverse
from devices.models import Device
from rest_framework import status

@pytest.mark.django_db
class TestDeleteDeviceAPI:
    
    def test_DELETE_device_status_204(self, authenticated_admin_client, device):
        client = authenticated_admin_client
        url = reverse('devices:delete', kwargs={'slug': device.slug})
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Device.objects.filter(slug=device.slug).exists()