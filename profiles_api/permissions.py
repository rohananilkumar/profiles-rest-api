from rest_framework import permissions

#base permission is the class that rest framework gives to create our own permissions
class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    #Every time a request is made, this function is called. View = view of the request, obj = object that the request is trying to access
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        #Safe methods are HTTP methods that is used to just view the objects (like OPTIONS and GET)
        if request.method in permissions.SAFE_METHODS:
            return True

        #Django automatically adds the user.id fields in the request object
        return obj.id == request.user.id