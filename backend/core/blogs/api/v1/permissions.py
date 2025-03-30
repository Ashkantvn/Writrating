from rest_framework.permissions import BasePermission


class IsAuthenticatedAndAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and getattr(request.user, 'is_admin', False)
    
    def has_object_permission(self, request, view, obj):
        return  request.user and request.user.is_authenticated and getattr(request.user, 'is_admin', False)
    

class IsAuthor(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        return obj.author.user == request.user