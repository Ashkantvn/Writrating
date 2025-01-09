import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from accounts.tests.fixtures import fake_user, authenticated_client


# test class
@pytest.mark.django_db
class TestAccountProfileAPI:
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
