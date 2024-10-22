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
    
    '''
    view:The view that is handling the request. Views in Django REST Framework handle 
    the logic of processing requests and returning responses. The view object can be used 
    to access additional information about how the request is being processed.

    obj:The object that the request is trying to access or modify. In the context of Django 
    REST Framework, this typically refers to a model instance that a view is dealing with. 
    For instance, if the view is used to handle requests for a User model, obj would be an 
    instance of User.
    '''