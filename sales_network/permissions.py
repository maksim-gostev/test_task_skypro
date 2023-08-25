from rest_framework import permissions


class IsActiveUserPermission(permissions.BasePermission):
    message = "Только активные пользователи имеют доступ к API"

    def has_permission(self, request, view):
        return request.user.is_active
