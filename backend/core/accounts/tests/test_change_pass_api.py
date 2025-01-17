import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from accounts.tests.fixtures import authenticated_client, fake_user


@pytest.mark.django_db
class TestChangePassAPI:
    def test_PATCH_change_pass_status_204(self, authenticated_client):
        url = reverse("accounts:changePassword")
        data = {
            "old_password": authenticated_client.password,
            "new_password": "Cawnodisj@#123",
            "new_password_confirm": "Cawnodisj@#123",
        }
        response = authenticated_client.patch(url, data=data)
        assert response.status_code == 204

        # Verify that the password has been changed
        user = authenticated_client.user
        user.refresh_from_db()
        assert user.check_password("Cawnodisj@#123") is True

    def test_PATCH_change_pass_status_401(self, fake_user):
        client = APIClient()
        url = reverse("accounts:changePassword")
        data = {
            "old_password": fake_user.password,
            "new_password": "Cawnodisj@#123",
            "new_password_confirm": "Cawnodisj@#123",
        }
        response = client.patch(url, data=data)
        assert response.status_code == 401

        # Verify that the password has not been changed
        fake_user.refresh_from_db()
        assert fake_user.check_password("Cawnodisj@#123") is False

    def test_PATCH_change_pass_status_403(self, authenticated_client):
        url = reverse("accounts:changePassword")
        data = {
            "old_password": "test",
            "new_password": "Cawnodisj@#123",
            "new_password_confirm": "Cawnodisj@#123",
        }
        response = authenticated_client.patch(url, data=data)
        assert response.status_code == 403

        data = {
            "old_password": "test",
            "new_password": "Cawnodisj@#123",
            "new_password_confirm": "disj@#123",
        }
        response = authenticated_client.patch(url, data=data)
        assert response.status_code == 403

        # Verify that the password has not been changed
        user = authenticated_client.user
        user.refresh_from_db()
        assert user.check_password("Cawnodisj@#123") is False

    def test_PATCH_change_pass_status_400(self, authenticated_client):
        url = reverse("accounts:changePassword")
        data = {
            "old_password": "",
            "new_password": "Cawnodisj@#123",
            "new_password_confirm": "Cawnodisj@#123",
        }
        response = authenticated_client.patch(url, data=data)
        assert response.status_code == 400

        # Verify that the password has not been changed
        user = authenticated_client.user
        user.refresh_from_db()
        assert user.check_password("Cawnodisj@#123") is False
