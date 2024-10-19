from rest_framework import permissions

class IsUserOrAdminOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return obj == request.user or obj == request.user.is_staff
        if request.method == "DELETE":
            return obj == request.user or obj == request.user.is_staff
        if request.method == "PUT":
            return obj == request.user 
        return False 