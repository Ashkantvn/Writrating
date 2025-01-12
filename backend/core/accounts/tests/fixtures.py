import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()


# fixtures
@pytest.fixture
def fake_user():
    user = User.objects.create_user(
        email="test10001@test.com", password="saodfh@#123WWE", is_active=True
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
    refreshToken = RefreshToken.for_user(user=user)
    accessToken = str(refreshToken.access_token)
    refreshToken = str(refreshToken)
    client.user = user
    client.access_token = accessToken
    client.refresh_token = refreshToken
    yield client
    user.delete()
