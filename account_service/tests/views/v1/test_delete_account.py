import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


@pytest.mark.django_db
class TestDeleteAccount:
    def setup_method(self):
        self.url = reverse("api:v1:delete_account")

    def test_POST_delete_account_status_204(self, authenticated_client):
        response = authenticated_client.post(self.url)
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_POST_delete_account_status_401(self):
        client = APIClient()
        response = client.post(self.url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
