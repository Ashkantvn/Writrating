import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


@pytest.fixture
def fake_user():
    user = User.objects.create_user(
        email="test10001@test.com", password="saodfh@#123WWE"
    )
    yield user
    user.delete()


@pytest.fixture
def authenticated_client():
    client = APIClient()
    user = User.objects.create_user(
        email="test10002@test.com", password="saodfh@#123WWE"
    )
    client.force_authenticate(
        user=user,
    )
    client.force_login(user=user)
    client.user = user
    yield client
    user.delete()


@pytest.mark.django_db
class TestAccountAPI:

    # Profile tests
    # Test for getting and updating profile data
    def test_GET_profile_api_response_200(self, fake_user):
        client = APIClient()
        url = reverse(
            "accounts:profile", kwargs={"username": fake_user.profile.username}
        )
        response = client.get(url)
        assert response.status_code == 200

    def test_GET_profile_api_reponse_404(self):
        client = APIClient()
        url = reverse("accounts:profile", kwargs={"username": "nothing"})
        response = client.get(url)
        assert response.status_code == 404

    def test_PATCH_profile_api_response_401(self, fake_user):
        client = APIClient()
        url = reverse(
            "accounts:profile", kwargs={"username": fake_user.profile.username}
        )
        response = client.patch(url, format="json", data={"username": "new test"})
        assert response.status_code == 401

    def test_PATCH_profile_api_reponse_403(self, authenticated_client, fake_user):
        url = reverse(
            "accounts:profile", kwargs={"username": fake_user.profile.username}
        )
        response = authenticated_client.patch(
            url, format="json", data={"username": "new test"}
        )
        assert response.status_code == 403

    def test_PATCH_profile_api_response_200(self, authenticated_client):
        user = authenticated_client.user
        url = reverse("accounts:profile", kwargs={"username": user.profile.username})
        response = authenticated_client.patch(
            path=url, format="json", data={"username": "newtest"}
        )
        assert response.status_code == 200
        assert response.data["username"] == "newtest"

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
