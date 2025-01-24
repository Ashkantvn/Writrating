import pytest
from fixtures import fake_user_with_recovery_digits, fake_user



@pytest.mark.django_db
class TestRecoveryDigitsValidationAPI:
    
    def test_POST_test_recovery_digits_validation_200(self,fake_user_with_recovery_digits):
        pass

    def test_POST_test_recovery_digits_validation_403(self,fake_user):
        pass

    def test_POST_test_recovery_digits_validation_400(self):
        pass