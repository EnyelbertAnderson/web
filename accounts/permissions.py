from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrSupervisor(BasePermission):
    """
    Permite solo a usuarios admin o supervisor crear, editar o borrar.
    Los demás solo pueden leer (GET, HEAD, OPTIONS).
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        user = request.user
        return user.is_authenticated and hasattr(user, 'role') and user.role in ['admin', 'supervisor']

class IsAdminOrSeller(BasePermission):
    """
    Permite a admin y cajero (vendedor) crear, editar o borrar.
    Los demás solo pueden leer.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        user = request.user
        return user.is_authenticated and hasattr(user, 'role') and user.role in ['admin', 'cajero']
