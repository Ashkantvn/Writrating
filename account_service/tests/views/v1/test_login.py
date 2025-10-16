import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

@pytest.mark.django_db
class TestLoginView:
    def setup_method(self):
        self.url = reverse("api:v1:login")
        self.client = APIClient()

    def test_POST_login_status_200(self,custom_user):
        data={
            "username":custom_user.username,
            "password":"tauefhmo@#$@%134423"
        }
        response= self.client.post(self.url,data)
        assert response.status_code == status.HTTP_200_OK
        keys = response.data.get("data").keys()
        assert "access_token" in keys, "response must have access token"
        assert "refresh_token" in keys, "response must have refresh token"

    def test_POST_login_status_404(self):
        data={
            "username":"custom_user.username",
            "password":"tauefhmo@#$@%134423"
        }
        response= self.client.post(self.url,data)
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data["detail"] == "User not found."

    def test_POST_status_400(self,custom_user):
        data={
            "username":custom_user.username,
            "password":"wrongpass"
        }
        response= self.client.post(self.url,data)
        assert response.status_code ==  status.HTTP_400_BAD_REQUEST
        assert response.data["detail"] == "Password is incorrect."
