import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from accounts.tests.fixtures import fake_user


@pytest.mark.django_db
class TestAccountLoginAPI:
    # Login tests
    # Test for POST data to server and login user
    def test_POST_login_user_200(self, fake_user):
        client = APIClient()
        url = reverse("accounts:login")
        response = client.post(
            url, data={"email": "test10001@test.com", "password": "saodfh@#123WWE"}
        )
        assert response.status_code == 200

    def test_POST_login_user_400(self, fake_user):
        client = APIClient()
        url = reverse("accounts:login")
        response = client.post(
            url,
            data={"password": "saodfh@#123WWE"},  # Send empty email field
        )
        assert response.status_code == 400

        response = client.post(
            url,
            data={"email": "test10001@test.com"},  # Send empty password field
        )
        assert response.status_code == 400

    def test_POST_login_user_401(self, fake_user):
        client = APIClient()
        url = reverse("accounts:login")
        response = client.post(
            url,
            data={  # Send different password
                "email": "test10001@test.com",
                "password": "saodfh@#",
            },
        )
        assert response.status_code == 401
