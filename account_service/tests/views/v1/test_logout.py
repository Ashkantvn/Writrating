import pytest
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.test import APIClient
from api.models import AccessTokenBlacklist


@pytest.mark.django_db
class TestLogoutView:
    def setup_method(self):
        self.url = reverse("api:v1:logout")

    def test_POST_logout_status_200(self, authenticated_client):
        refresh_token = RefreshToken().for_user(authenticated_client.user)
        access_token = refresh_token.access_token
        data = {"access_token": access_token, "refresh_token": refresh_token}
        response = authenticated_client.post(self.url, data)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert response.data is None, "response.data should not be available."
        # Check access token is blacklist now
        access_token_blacklist = AccessTokenBlacklist.objects.filter(
            jti=access_token["jti"]
        ).exists()
        assert access_token_blacklist, "access token must be in blacklist."

    def test_POST_logout_status_401(self):
        client = APIClient()
        data = {"access_token": "token", "refresh_token": "token"}
        response = client.post(self.url, data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_POST_logout_status_400(self, authenticated_client):
        data = {
            "access_token": "token",
            "refresh_token": "token",
        }
        response = authenticated_client.post(self.url, data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data.get("detail") == "Invalid token."
