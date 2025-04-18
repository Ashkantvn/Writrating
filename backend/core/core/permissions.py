from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


class IsAuthenticatedAndAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and getattr(request.user, "is_admin", False)
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.user
            and request.user.is_authenticated
            and getattr(request.user, "is_admin", False)
        )


class IsAuthor(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.author.user == request.user


class IsValidator(BasePermission):
    def has_permission(self, request, view):
        return getattr(request.user, "is_validator", False)

    def has_object_permission(self, request, view, obj):
        return getattr(request.user, "is_validator", False)


class IsValidatorForGET(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET" and not getattr(request.user, "is_validator", False):
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.method == "GET" and not getattr(request.user, "is_validator", False):
            return False
        return True
