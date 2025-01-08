from rest_framework.permissions import BasePermission, SAFE_METHODS
from accounts.api.v1.exceptions import CustomAuthenticationFailed


class CustomIsAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif not request.user or not request.user.is_authenticated:
            raise CustomAuthenticationFailed()
        else:
            return True
