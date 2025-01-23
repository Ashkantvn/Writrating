import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from accounts.tests.fixtures import fake_user

@pytest.mark.django_db
class TestPasswordRecoveryAPI:
    def test_POST_password_recovery_status_201(self,fake_user):
        client =  APIClient()
        url = reverse("accounts:passwordRecovery")
        data = {
            "email": fake_user.email
        }
        response = client.post(url,data=data)
        assert response.status_code == 201
        

    def test_POST_password_recovery_status_400(self):
        client =  APIClient()
        url = reverse("accounts:passwordRecovery")

        data = {
            "email": ""
        }
        response = client.post(url,data=data)

        assert response.status_code == 400

        data = {
            "email": "test"
        }
        response = client.post(url,data=data)

        assert response.status_code == 400


    def test_POST_password_recovery_status_404(self):
        client =  APIClient()
        url = reverse("accounts:passwordRecovery")

        data = {
            "email": "others@other.com"
        }
        response = client.post(url,data=data)

        assert response.status_code == 404