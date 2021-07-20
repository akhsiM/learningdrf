from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    '''

    Only owner has read-write.

    '''

    def has_object_permission(self, request, view, obj):
        # read permissions are allowed for any request
        # so -> always allow GET, HEAD or OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # write permission for owner only
        return obj.owner == request.user