import pytest
from accounts.tests.fixtures import authenticated_client
from django.urls import reverse
from rest_framework.test import APIClient

@pytest.mark.django_db
class TestDeleteAccountAPI:
    def test_DELETE_delete_account_status_204(self,authenticated_client):
        url = reverse("accounts:deleteAccount")
        response = authenticated_client.delete(path=url)
        assert response.status_code == 204

    def test_DELETE_delete_account_status_401(self):
        client = APIClient()
        url = reverse("accounts:deleteAccount")
        response = client.delete(path=url)
        assert response.status_code == 401
        
