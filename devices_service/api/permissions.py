from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):
    """
    Allow access only to Django superusers.
    """

    def has_permission(self, request, view):
        user = getattr(request, "user", None)
        return bool(user and user.is_authenticated and user.is_superuser)

    def has_object_permission(self, request, view, obj):
        user = getattr(request, "user", None)
        return bool(user and user.is_authenticated and user.is_superuser)
