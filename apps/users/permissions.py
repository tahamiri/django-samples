from rest_framework.permissions import BasePermission


class IsSelfOrAdmin(BasePermission):
    """
    Allow users to access/modify their own object,
    or allow admins full access.
    """

    def has_object_permission(self, request, view, obj):
        # Admins can do everything
        if request.user and request.user.is_staff:
            return True

        # Users can only access their own object
        return obj == request.user