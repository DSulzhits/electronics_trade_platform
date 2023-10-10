from rest_framework.permissions import BasePermission
from users.models import UserRoles


class IsModerator(BasePermission):
    """Add custom permission for User.role Moderator
    (Добавлено дополнительное право доступа User.role Moderator)"""
    message = "Only for moderator"

    def has_permission(self, request, view):
        if request.user.role == UserRoles.MODERATOR:
            return True
        return False


class IsSuperuser(BasePermission):
    """Add custom permission for superuser
    (Добавлено дополнительное право доступа superuser)"""
    message = "Only for administrator"

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False


class IsActive(BasePermission):
    """Add custom permission for active users
    (Добавлено дополнительное право доступа для активных пользователей"""
    message = "User is not active, please contact the service administration"

    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        return False
