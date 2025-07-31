from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
    Permite solo a usuarios admin (role='admin') crear, editar o borrar.
    Los demás solo pueden leer (GET, HEAD, OPTIONS).
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        user = request.user
        return user.is_authenticated and hasattr(user, 'role') and user.role == 'admin'
