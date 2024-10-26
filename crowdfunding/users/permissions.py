from rest_framework import permissions

class IsUserOrAdminOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return obj == request.user or request.user.is_superuser
        if request.method == "DELETE":
            return obj == request.user or request.user.is_superuser
        if request.method == "PUT":
            return obj == request.user or request.user.is_superuser
        return False 