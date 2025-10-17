import pytest
from django.urls import reverse
from rest_framework import status

@pytest.mark.django_db
class TestCreateProfileView:
    def setup_method(self):
        self.url = reverse("api:v1:create_profile")

    def test_POST_create_profile_status_201(self, superuser_client):
        response = superuser_client.post(self.url, data={
            "username": "newuser",
        })
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["data"] == "Profile created successfully."

    def test_POST_create_profile_status_401(self, normal_user_client):
        response = normal_user_client.post(self.url, data={
            "username": "newuser",
        })
        assert response.status_code == status.HTTP_403_FORBIDDEN