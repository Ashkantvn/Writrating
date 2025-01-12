import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from accounts.tests.fixtures import authenticated_client,fake_user
from rest_framework_simplejwt.tokens import RefreshToken

@pytest.mark.django_db
class TestAccountLogoutAPI:
    def test_POST_logout_user_204(self,authenticated_client):
        access_token = authenticated_client.access_token
        refresh_token = authenticated_client.refresh_token
        data = {
            "access_token":access_token,
            "refresh_token":refresh_token
        }
        url = reverse("accounts:logout")
        response = authenticated_client.post(url,data=data)
        assert response.status_code == 204

    def test_POST_logout_user_401(self):
        client = APIClient()
        url = reverse("accounts:logout")
        response = client.post(url,data={
            "access_token":"token",
            "refresh_token":"refresh_token"
        }) 
        assert response.status_code == 401

    def test_POST_logout_user_403(self,authenticated_client,fake_user):
        refresh_token = RefreshToken.for_user(fake_user)
        access_token = str(refresh_token.access_token)
        refresh_token = str(refresh_token)
        url = reverse("accounts:logout")
        data={
            "access_token":access_token,
            "refresh_token":refresh_token
        }
        response = authenticated_client.post(url,data=data)
        assert response.status_code == 403

    def test_POST_logout_user_400(self,authenticated_client):
        url = reverse("accounts:logout")

        response = authenticated_client.post(url,data={
            "access_token": "",
            "refresh_token": ""
        }) 
        assert response.status_code == 400

        response = authenticated_client.post(url,data={
            "access_token":"token",
            "refresh_token":""
        })
        assert response.status_code == 400

        response = authenticated_client.post(url,data={
            "access_token":"",
            "refresh_token":"token"
        })
        assert response.status_code == 400


        