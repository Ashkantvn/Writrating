import pytest
from django.contrib.auth import get_user_model
from api.models import AccessTokenBlacklist
from rest_framework.test import APIClient

User = get_user_model()

@pytest.fixture()
def custom_user(db):
    user = User.objects.create_user(
        username="test",
        password="tauefhmo@#$@%134423",
    )
    yield user
    if user.pk:
        user.delete()

@pytest.fixture()
def access_token_blacklist(db):
    blacklist = AccessTokenBlacklist.objects.create(
        jti="wodjamlwijef@#$2323"
    )
    yield blacklist
    if blacklist.pk:
        blacklist.delete()

@pytest.fixture()
def authenticated_client(db):
    user = User.objects.create_user(
        username="test2",
        password="afwoicwm@#$133124"
    )
    client = APIClient()
    client.force_authenticate(user=user)
    client.user = user
    yield client
    if user.pk:
        user.delete()

