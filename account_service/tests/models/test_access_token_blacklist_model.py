import pytest


@pytest.mark.django_db
class TestAccessTokenBlackList:
    def test_access_token_black_list_is_created(self, access_token_blacklist):
        # Check blacklist jti is str
        blacklist_jti_is_str = isinstance(access_token_blacklist.jti, str)
        assert blacklist_jti_is_str, "Blacklist jti is not str"
        # Check blacklist created_date and updated_date
        assert access_token_blacklist.created_at is not None
        assert access_token_blacklist.updated_at is not None

    def test_access_token_black_list_str(self, access_token_blacklist):
        assert str(access_token_blacklist) == access_token_blacklist.jti
