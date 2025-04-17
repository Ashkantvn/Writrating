import pytest 
from django.urls import reverse, resolve
from rest_framework import status
from user_interactions.api.v1 import views
from user_interactions.tests.fixtures import first_device,second_device,authenticated_client
from rest_framework.test import APIClient

@pytest.mark.django_db
class TestCompareDevices:

    def test_compare_devices_is_resolve(self):
        url = reverse("interactions:compare-devices", kwargs={"slug1": "test1", "slug2": "test2"})
        view_class = resolve(url).func.view_class
        assert view_class == views.CompareDevicesAPIView

    def test_GET_compare_devices_status_200(self,authenticated_client,first_device,second_device):
        client = authenticated_client
        url = reverse("interactions:compare-devices", kwargs={"slug1": first_device.slug, "slug2": second_device.slug})
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_GET_compare_devices_status_404(self,authenticated_client):
        client = authenticated_client
        url = reverse("interactions:compare-devices", kwargs={"slug1": "test1", "slug2": "test2"})
        response = client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_GET_compare_devices_status_401(self,first_device,second_device):
        client = APIClient()
        url = reverse("interactions:compare-devices", kwargs={"slug1": first_device.slug, "slug2": second_device.slug})
        response = client.get(url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_GET_compare_devices_status_400(self,authenticated_client,first_device):
        client = authenticated_client
        url = reverse("interactions:compare-devices", kwargs={"slug1": first_device.slug, "slug2": first_device.slug})
        response = client.get(url)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["detail"] == "The devices are the same"
