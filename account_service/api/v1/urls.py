from rest_framework_simplejwt.views import TokenRefreshView
from api.v1.views import (
    Logout,
    SignUp,
    VerifyAccessToken,
    ChangePass,
    CustomTokenObtainPairView,
    DeleteAccount,
)
from django.urls import path

app_name = "v1"

urlpatterns = [
    path(
        "account/login/",
        CustomTokenObtainPairView.as_view(),
        name="token_obtain_pair"
    ),
    path(
        "account/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh"
    ),
    path(
        "account/token/verify/",
        VerifyAccessToken.as_view(),
        name="verify_access_token"
    ),
    path("account/signup/", SignUp.as_view(), name="signup"),
    path("account/logout/", Logout.as_view(), name="logout"),
    path("account/change-pass/", ChangePass.as_view(), name="change-pass"),
    path(
        "account/delete-account/",
        DeleteAccount.as_view(),
        name="delete_account"
    ),
]
