from rest_framework.exceptions import APIException
from rest_framework import status


class CustomAuthenticationFailed(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Authentication credentials were not provided."
    default_code = "authentication_failed"
