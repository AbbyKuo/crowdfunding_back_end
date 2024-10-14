from rest_framework import permissions
from .models import CustomUser

class IsUserOrAdminOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return obj == request.user or request.user.is_staff
        return False