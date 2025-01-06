from django.shortcuts import render
from rest_framework.generics import GenericAPIView

# Create your views here.
class ProfileAPI(GenericAPIView):
    pass

class SignUpAPI(GenericAPIView):
    pass

class LoginAPI(GenericAPIView):
    pass

class LogoutAPI(GenericAPIView):
    pass

class DeleteAccountAPI(GenericAPIView):
    pass

class ChangePassAPI(GenericAPIView):
    pass

class PasswordRecoveryAPI(GenericAPIView):
    pass

class PasswordRecoveryVerificationAPI(GenericAPIView):
    pass