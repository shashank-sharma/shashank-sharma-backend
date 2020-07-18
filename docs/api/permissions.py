from rest_framework import permissions


class IsAdminOrSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if (hasattr(request.user, 'is_admin') and request.user.is_admin) or \
                (hasattr(request.user, 'is_superuser') and request.user.is_superuser):
            return True
        else:
            return False

