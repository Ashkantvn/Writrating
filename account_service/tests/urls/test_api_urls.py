import pytest
from django.urls import reverse, resolve
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from api.v1 import views

@pytest.mark.django_db
class TestAccountUrls:
    def test_token_obtain_url_is_resolved(self):
        url = reverse("api:v1:token_obtain_pair")
        view_class= resolve(url).func.view_class
        assert view_class == TokenObtainPairView

    def test_refresh_token_is_resolved(self):
        url = reverse("api:v1:token_refresh")
        view_class= resolve(url).func.view_class
        assert view_class == TokenRefreshView

    def test_verify_token_is_resolved(self):
        url = reverse("api:v1:verify_access_token")
        view_class= resolve(url).func.view_class
        assert view_class == views.VerifyAccessToken

    def test_logout_token_is_resolved(self):
        url = reverse("api:v1:logout")
        view_class= resolve(url).func.view_class
        assert view_class == views.Logout

    def test_logout_token_is_resolved(self):
        url = reverse("api:v1:login")
        view_class= resolve(url).func.view_class
        assert view_class == views.Login

    def test_sign_up_is_resolve(self):
        url = reverse("api:v1:signup")
        view_class= resolve(url).func.view_class
        assert view_class == views.SignUp

    def test_change_pass_is_resolve(self):
        url = reverse("api:v1:change-pass")
        view_class= resolve(url).func.view_class
        assert view_class == views.ChangePass
    