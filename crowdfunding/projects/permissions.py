from rest_framework import permissions
from .models import Project

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class IsSupporterOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (obj.supporter == request.user) and (obj.supporter != obj.project.owner)

## For supporter who can't be the project owner
class IsSupporterOrReadOnlyAndNotOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        project_pk = request.data["project"]
        project = Project.objects.get(pk=project_pk)
        return request.user != project.owner