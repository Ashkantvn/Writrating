import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import status

@pytest.mark.django_db
class TestVerifyAccessToken:
    def setup_method(self):
        self.url = reverse("api:v1:verify_access_token")
        self.client = APIClient()

    def test_POST_status_200(self, custom_user):
        access_token = AccessToken.for_user(custom_user)
        data={
            "access_token":str(access_token),
        }
        response = self.client.post(self.url,data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["data"] == str(access_token)

    def test_POST_status_400(self):
        data={
            "access_token":"str(access_token)",
        }
        response = self.client.post(self.url,data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["detail"] == "Invalid token."