from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True  # Разрешаем доступ для метода POST
        elif request.method == 'GET':
            return request.user and request.user.is_authenticated  # Проверяем аутентификацию для метода GET
        return False  # Запрещаем доступ для других методов
