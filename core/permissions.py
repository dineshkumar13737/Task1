from rest_framework import permissions
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.permissions import DjangoModelPermissions

# Create a combined permission class
class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.roles.filter(name='Manager').exists()

class IsMember(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

class IsSuperAdminOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and (request.user.is_superuser or request.user.is_staff)