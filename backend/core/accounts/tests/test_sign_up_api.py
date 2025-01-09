import pytest
from rest_framework.test import APIClient
from django.urls import reverse


@pytest.mark.django_db
class TestAccountSignUpAPI:
    # Sign-up tests
    # Test for post data to server and register new user
    def test_POST_sign_up_api_response_201(self):
        client = APIClient()
        url = reverse("accounts:signup")
        response = client.post(
            url,
            data={
                "email": "test@test.com",
                "password": "wcofn@#!@#1234",
                "password_confirm": "wcofn@#!@#1234",
            },
        )
        assert response.status_code == 201

    def test_POST_sign_up_api_response_400(self):
        client = APIClient()
        url = reverse("accounts:signup")
        response = client.post(  # Post data with different passwords
            url,
            data={
                "email": "test@test.com",
                "password": "dasofjn@#$123",
                "password_confirm": "sodfojoj@#$443",
            },
        )
        assert response.status_code == 400

        response = client.post(  # Post data with invalid email
            url,
            data={
                "email": "test",
                "password": "dasofjn@#$123",
                "password_confirm": "sodfojoj@#$443",
            },
        )
        assert response.status_code == 400
