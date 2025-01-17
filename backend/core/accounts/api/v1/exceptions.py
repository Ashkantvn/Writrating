from rest_framework.exceptions import APIException
from rest_framework import status


class PermissionDeniedException(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "Permission denied. "
    default_code = "Permission denied. "
