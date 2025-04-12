import pytest
from devices.tests.fixtrues import validator_client, device, authenticated_admin_client, admin
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
class TestCheckDeviceAPI:

    def test_PATCH_check_device_status_200(self, validator_client, device):
        client = validator_client
        url = reverse('devices:check', kwargs={'slug': device.slug})
        response = client.patch(url,data={'publishable':True})
        assert response.status_code == status.HTTP_200_OK
        device.refresh_from_db()
        assert device.publishable

    def test_PATCH_check_device_status_404(self, validator_client):
        client = validator_client
        url = reverse('devices:check', kwargs={'slug': 'non-existent-slug'})
        response = client.patch(url,data={'publishable':True})
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_PATCH_check_device_status_401(self, device):
        client = APIClient()
        url = reverse('devices:check', kwargs={'slug': device.slug})
        response = client.patch(url,data={'publishable':True})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        device.refresh_from_db()
        assert not device.publishable

    def test_PATCH_check_device_status_403(self, authenticated_admin_client, device):
        client = authenticated_admin_client
        url = reverse('devices:check', kwargs={'slug': device.slug})
        response = client.patch(url,data={'publishable':True})
        assert response.status_code == status.HTTP_403_FORBIDDEN
        device.refresh_from_db()
        assert not device.publishable

    
    # POST method tests
    def test_POST_check_device_status_201(self, validator_client, device, admin):
        client = validator_client
        url = reverse('devices:check', kwargs={'slug': device.slug})
        data = {
            'title': 'Test title',
            'content': 'Test content',
        }
        response = client.post(url,data=data)
        assert response.status_code == status.HTTP_201_CREATED


    def test_POST_check_device_status_404(self, validator_client):
        client = validator_client
        url = reverse('devices:check', kwargs={'slug': 'non-existent-slug'})
        data = {
            'title': 'Test title',
            'content': 'Test content',
        }
        response = client.post(url,data=data)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_POST_check_device_status_401(self, device):
        client = APIClient()
        url = reverse('devices:check', kwargs={'slug': device.slug})
        response = client.post(url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_POST_check_device_status_403(self, authenticated_admin_client, device,admin):
        client = authenticated_admin_client
        url = reverse('devices:check', kwargs={'slug': device.slug})
        data = {
            'title': 'Test title',
            'content': 'Test content',
        }
        response = client.post(url,data=data)
        assert response.status_code == status.HTTP_403_FORBIDDEN