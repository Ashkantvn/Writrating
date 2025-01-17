from django.urls import path
from accounts.api.v1 import views
from rest_framework_simplejwt import views as simplejwt_views

app_name = "accounts"

urlpatterns = [
    path("profile/<str:username>/", views.ProfileAPI.as_view(), name="profile"),
    path("sign-up/", views.SignUpAPI.as_view(), name="signup"),
    path("login/", simplejwt_views.TokenObtainPairView.as_view(), name="login"),
    path(
        "token/refresh",
        simplejwt_views.TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path("logout/", views.LogoutAPI.as_view(), name="logout"),
    path("delete-account/", views.DeleteAccountAPI.as_view(), name="deleteAccount"),
    path("change-password/", views.ChangePassAPI.as_view(), name="changePassword"),
    path(
        "password-recovery/",
        views.PasswordRecoveryAPI.as_view(),
        name="passwordRecovery",
    ),
    path(
        "password-recovery/<str:email>/<int:code>",
        views.PasswordRecoveryVerificationAPI.as_view(),
        name="passwordRecoveryVerification",
    ),
]
