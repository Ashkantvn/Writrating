import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
class TestChangePassView:
    def setup_method(self):
        self.url = reverse("api:v1:change-pass")

    def test_change_pass_status_200(self, authenticated_client):
        data = {
            "new_password": "awioejfm@#$1235",
            "new_password_confirm": "awioejfm@#$1235",
        }
        response = authenticated_client.post(self.url, data)
        assert response.status_code == status.HTTP_200_OK

    def test_change_pass_status_400(self, authenticated_client):
        data = {
            "new_password": "awioejfm5",
            "new_password_confirm":
            "awioejfm@#$1235"
        }
        response = authenticated_client.post(self.url, data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        detail = response.data.get("detail")
        assert detail == "Password and password confirm mismatch."

    def test_change_pass_status_weak_password_400(self, authenticated_client):
        data = {"new_password": "password", "new_password_confirm": "password"}
        response = authenticated_client.post(self.url, data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        detail = response.data.get("detail")
        assert detail == "Weak password."
