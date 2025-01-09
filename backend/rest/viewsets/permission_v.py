from rest_framework.permissions import BasePermission
class IsAdmin(BasePermission):
    """
    Разрешение для администраторов.
    """

    def has_permission(self, request, view):
        # Проверяем, является ли пользователь администратором
        return request.user.role == 'admin'


class IsClient(BasePermission):
    """
    Разрешение для клиентов.
    """

    def has_permission(self, request, view):
        # Проверяем, является ли пользователь клиентом
        return request.user.role == 'client'