import pytest
from accounts.tests.fixtures import fake_user_with_recovery_digits, fake_user
from rest_framework.test import APIClient
from django.urls import reverse
from accounts.models import RecoveryCode

@pytest.mark.django_db
class TestRecoveryDigitsValidationAPI:
    
    def test_POST_test_recovery_digits_validation_200(self,fake_user_with_recovery_digits):
        client = APIClient()
        url = reverse('accounts:passwordRecoveryValidation')
        data = {
            "email": fake_user_with_recovery_digits.email,
            "digits": fake_user_with_recovery_digits.digits,
            "new_password": "nacdsfoim@#1234WER",
            "new_password_confirm": "nacdsfoim@#1234WER"
        }
        response = client.post(url, data=data)
        assert response.status_code == 200

        user = fake_user_with_recovery_digits
        user.refresh_from_db()
        assert user.check_password("nacdsfoim@#1234WER") is True

        has_recovery_code = RecoveryCode.objects.filter(user=user).exists()
        assert has_recovery_code == False

    def test_POST_test_recovery_digits_validation_403(self,fake_user,fake_user_with_recovery_digits):
        client = APIClient()
        url = reverse('accounts:passwordRecoveryValidation')
        data = {
            "email": fake_user.email,
            "digits": fake_user_with_recovery_digits.digits,
            "new_password": "woecfhnoij@#$1234WER",
            "new_password_confirm": "woecfhnoij@#$1234WER"
        }
        response = client.post(url, data=data)
        assert response.status_code == 403

        user = fake_user
        user.refresh_from_db()
        assert user.check_password("woecfhnoij@#$1234WER") is False

        has_recovery_code = RecoveryCode.objects.filter(user=fake_user_with_recovery_digits).exists()
        assert has_recovery_code == True

    def test_POST_test_recovery_digits_validation_400(self):
        client = APIClient()
        url = reverse('accounts:passwordRecoveryValidation')
        data = {
            "email": "test@test.com",
            "digits": 4444565,
            "new_password": "woecfhnoij@#$1234WER",
            "new_password_confirm": "woecfhnoij@#$1234WER"
        }
        response = client.post(url, data=data)
        assert response.status_code == 400

        data = {
            "email": "test",
            "digits": 4444,
            "new_password": "woecfhnoij@#$1234WER",
            "new_password_confirm": "woecfhnoij@#$1234WER"
        }
        response = client.post(url, data=data)
        assert response.status_code == 400

        data = {
            "email": "test@test.com",
            "digits": 4444,
            "new_password": "woecfhno$1234WER",
            "new_password_confirm": "woecfhnoij@#$1234WER"
        }
        response = client.post(url, data=data)
        assert response.status_code == 400