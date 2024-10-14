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
        print("HTTP Request body", request.data)
        # Get the pk from HTTP Request body (dictionary)
        project_pk = request.data["project"]  # 1
        print("project_pk", project_pk)
        # Get the Project model data from the database
        project = Project.objects.get(pk=project_pk)
        print("project", project)
        print("request.user", request.user)
        print("project.owner", project.owner)
        # Token for user 1
        return request.user != project.owner