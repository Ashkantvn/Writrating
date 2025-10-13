import pytest
from django.contrib.auth import get_user_model
from api.models import AccessTokenBlacklist

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
        code="wodjamlwijef@#$2323"
    )
    yield blacklist
    if blacklist.pk:
        blacklist.delete()
