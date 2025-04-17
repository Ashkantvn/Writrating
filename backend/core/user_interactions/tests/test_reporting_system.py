import pytest 
from django.urls import reverse, resolve
from rest_framework import status
from user_interactions.api.v1 import views
from rest_framework.test import APIClient
from user_interactions.tests.fixtures import authenticated_client,validator_client,admin_client
from user_interactions import models

@pytest.mark.django_db
class TestReportingSystem:

    def test_reporting_system_is_resolved(self):
        url = reverse("interactions:report")
        view_class = resolve(url).func.view_class
        assert view_class == views.ReportingSystemAPIView

    def test_POST_reporting_system_status_201(self, authenticated_client):
        client = authenticated_client
        url = reverse("interactions:report")
        data = {
            "report_title": "Test bug report",
            "report_content": "test-device-slug",
        }
        response = client.post(url, data=data)
        assert response.status_code == status.HTTP_200_OK
        assert models.Report.objects.filter(report_title="Test bug report").exists()

    def test_POST_reporting_system_status_401(self):
        client = APIClient()
        url = reverse("interactions:report")
        data = {
            "report_title": "Test bug report",
            "report_content": "test-device-slug",
        }
        response = client.post(url, data=data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert not models.Report.objects.filter(report_title="Test bug report").exists()

    # test GET method
    def test_GET_reporting_system_status_401(self):
        client = APIClient()
        url = reverse("interactions:report")
        response = client.get(url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_GET_reporting_system_status_200(self, validator_client):
        client = validator_client
        url = reverse("interactions:report")
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_GET_reporting_system_status_403(self, admin_client):
        client = admin_client
        url = reverse("interactions:report")
        response = client.get(url)
        assert response.status_code == status.HTTP_403_FORBIDDEN


    

    
