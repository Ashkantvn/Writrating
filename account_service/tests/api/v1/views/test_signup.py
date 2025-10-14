import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse

@pytest.mark.django_db
class TestSignUp:
    def setup_method(self):
        self.client = APIClient()
        self.url = reverse("api:v1:signup")

    def test_POST_signup_status_201(self):
        data={
            "username":"testuser",
            "password":"awoeifjcj@#@$%32145",
            "password_confirm": "awoeifjcj@#@$%32145"
        }
        response = self.client.post(
            self.url,
            data
        )
        assert response.status_code == status.HTTP_201_CREATED
        # Check access token
        string_access_token = isinstance(
            response.data["data"]["access"],
            str
        )
        assert string_access_token, "Access token must be string"
        # Check refresh token
        string_refresh_token = isinstance(
            response.data["data"]["refresh"],
            str
        )
        assert string_refresh_token, "Refresh token must be string"

    def test_POST_signup_exist_user_status_400(self,custom_user):
        data={
            "username":custom_user.username,
            "password":"awoeifjcj@#@$%32145",
            "password_confirm": "awoeifjcj@#@$%32145"
        }
        response= self.client.post(self.url,data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["detail"] == "User exists."

    def test_POST_signup_different_password_status_400(self):
        data={
            "username":"testuser",
            "password":"asldjf@#4123",
            "password_confirm":"oasdjfw@#23"
        }
        response= self.client.post(self.url,data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["detail"] == "Password and password confirm mismatch."

    def test_POST_signup_weak_password_status_400(self):
        data={
            "username":"testuser",
            "password":"pass",
            "password_confirm":"pass",
        }
        response = self.client.post(self.url,data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["detail"] == "Weak password."