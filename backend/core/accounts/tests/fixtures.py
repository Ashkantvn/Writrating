import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.models import RecoveryCode


User = get_user_model()


# fixtures
@pytest.fixture
def fake_user():
    email = "test10001@test.com"
    password = "saodfh@#123WWE"

    user = User.objects.create_user(email=email, password=password, is_active=True)

    user.password = password
    user.email = email

    yield user
    user.delete()


@pytest.fixture
def authenticated_client():
    email = "test10002@test.com"
    password = "saodfh@#123WWE"

    client = APIClient()
    user = User.objects.create_user(email=email, password=password)
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
    client.password = password

    yield client

    user.delete()


@pytest.fixture
def fake_user_with_recovery_digits():
    email = "test10003@test.com"
    password = "apowem@#$1234WER"

    user = User.objects.create_user(email=email, password=password, is_active=True)
    recovery_code = RecoveryCode.objects.create(user=user, digits=1234)

    user.digits = recovery_code.digits
    user.email = email

    yield user
    user.delete()
    recovery_code.delete()

    
