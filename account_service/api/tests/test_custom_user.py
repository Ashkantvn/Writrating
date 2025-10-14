import pytest

@pytest.mark.django_db
class TestCustomUser:
    def test_custom_user_is_created(self,custom_user):
        username_is_str = isinstance(custom_user.username,str)
        assert username_is_str,"username must be string"
        assert custom_user.is_superuser == False, "Super user is not false"
        # Check created_at and updated_at is not none
        assert custom_user.created_at is not None 
        assert custom_user.updated_at is not None

    def test_custom_user_str(self,custom_user):
        assert str(custom_user) == custom_user.username