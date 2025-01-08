from django.urls import path
from accounts.api.v1 import views

app_name = "accounts"

urlpatterns = [
    path("profile/<str:username>/", views.ProfileAPI.as_view(), name="profile"),
    path("sign-up/", views.SignUpAPI.as_view(), name="signUp"),
    path("login/", views.LoginAPI.as_view(), name="login"),
    path("logout/", views.LogoutAPI.as_view(), name="logout"),
    path("delete-account/", views.DeleteAccountAPI.as_view(), name="deleteAccount"),
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
