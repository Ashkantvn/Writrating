import pytest
from accounts.tests.fixtures import authenticated_client, fake_user
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

@pytest.mark.django_db
class TestDeleteAccountAPI:
    def test_DELETE_delete_account_status_204(self,authenticated_client):
        url = reverse("accounts:deleteAccount")
        data = {
            "access_token": authenticated_client.access_token,
            "refresh_token": authenticated_client.refresh_token,
        }
        response = authenticated_client.delete(path=url,data=data)
        assert response.status_code == 204

    def test_DELETE_delete_account_status_401(self):
        client = APIClient()
        url = reverse("accounts:deleteAccount")
        data = {
            "access_token":"token",
            "refresh_token":"token"
        }
        response = client.delete(path=url,data=data)
        assert response.status_code == 401

    def test_DELETE_delete_account_status_403(self,authenticated_client,fake_user):
        refresh_token = RefreshToken.for_user(fake_user)
        access_token = str(refresh_token.access_token)
        refresh_token = str(refresh_token)
        url = reverse("accounts:deleteAccount")
        data = {
            "access_token": access_token,
            "refresh_token": refresh_token,
        }
        response = authenticated_client.delete(path=url,data=data)
        assert response.status_code == 403
        
