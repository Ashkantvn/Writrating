import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


@pytest.fixture
def fake_user():
    user = User.objects.get_or_create(
        email= "test2@test.com",
    )[0]
    user.set_password("saodfh@#123WWE")
    user.profile.username = "test2"
    user.save()
    yield user
    user.delete()
    
@pytest.fixture
def authenticated_client():
    client = APIClient()
    user = User.objects.get_or_create(
        email= "test@test.com",
    )[0]
    user.set_password("saodfh@#123WWE")
    user.profile.username = "test"
    user.save()
    user = User.objects.get(email="test@test.com")
    client.force_login(user)
    yield client 
    user.delete()

@pytest.mark.django_db
class TestAccountAPI:

    # Profile tests
    # Test for getting and updating profile data
    def test_GET_profile_api_response_200(self):
        client = APIClient()
        url = reverse("accounts:profile",kwargs={"username":"test"})
        response = client.get(url)
        assert response.status_code == 200

    def test_PATCH_profile_api_response_401(self):
        client = APIClient()
        url = reverse("accounts:profile",kwargs={"username":"test"})
        response = client.patch(url,format="json",data={
            "profile":{
                "username":"new test"
            }
        })
        assert response.status_code == 401

    def test_PATCH_profile_api_reponse_403(self,authenticated_client,fake_user):
        url = reverse("accounts:profile",kwargs={"username":fake_user.profile.username})
        response = authenticated_client.patch(url,format="json",data={
            "profile":{
                "username":"new test"
            }
        })
        assert response.status_code == 403

    def test_PATCH_profile_api_response_200(self,authenticated_client):
        url = reverse("accounts:profile",kwargs={"username":"test"})
        response = authenticated_client.patch(url,format="json",data={
            "profile":{
                "username":"new test"
            }
        })
        assert response.status_code == 200



