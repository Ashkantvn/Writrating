from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView
)
from api.v1.views import(
    Logout,
    SignUp,
    VerifyAccessToken,
    Login,
    ChangePass
)
from django.urls import path

app_name="v1"

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", VerifyAccessToken.as_view(), name="verify_access_token"),
    path("token/signup/", SignUp.as_view(), name="signup"),
    path("token/logout/", Logout.as_view(), name="logout"),
    path("token/login/", Login.as_view(), name="login"),
    path("token/change-pass/", ChangePass.as_view(), name="change-pass"),
]
