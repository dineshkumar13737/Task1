from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import User, Organization, Role
from .serializers import UserSerializer, OrganizationSerializer, RoleSerializer
from .permissions import IsSuperAdmin, IsAdmin, IsManager, IsMember, IsSuperAdminOrAdmin

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    def get_permissions(self):
        if self.action in ['create']:
            return [IsSuperAdminOrAdmin()]  
        elif self.action in ['update', 'partial_update']:
            if self.request.user.is_superuser:
                return [IsSuperAdmin()]
            elif self.request.user.is_staff:  
                return [IsAdmin()]
            return []  
        elif self.action in ['destroy']:
            if self.request.user.is_superuser:
                return [IsSuperAdmin()]
            elif self.request.user.is_staff:  
                return [IsAdmin()]
            return []  
        return super().get_permissions()

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def get_permissions(self):
        if self.action in ['create']:
            return [IsSuperAdminOrAdmin()] 
        elif self.action in ['update', 'partial_update']:
            if self.request.user.is_superuser:
                return [IsSuperAdmin()]
            elif self.request.user.is_staff:  
                return [IsAdmin()]
            return []  
        elif self.action in ['destroy']:
            if self.request.user.is_superuser:
                return [IsSuperAdmin()]
            elif self.request.user.is_staff:  
                return [IsAdmin()]
            return []  
        return super().get_permissions()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['create']:
            return [IsSuperAdminOrAdmin()]  
        elif self.action in ['update', 'partial_update']:
            if self.request.user.is_superuser:
                return [IsSuperAdmin()]
            elif self.request.user.is_staff:  
                return [IsAdmin()]
            elif self.request.user.is_authenticated and self.request.user.roles.filter(name='Manager').exists():
                return [IsManager()]  
            return [IsMember()]  
        elif self.action in ['destroy']:
            if self.request.user.is_superuser:
                return [IsSuperAdmin()]
            elif self.request.user.is_staff:  
                return [IsAdmin()]
            return []  
        elif self.action in ['list']:
            if self.request.user.is_superuser:
                return [IsSuperAdmin()]
            elif self.request.user.is_staff:  
                return [IsAdmin()]
            elif self.request.user.is_authenticated and self.request.user.roles.filter(name='Manager').exists():
                return [IsManager()]  
            return []  
        elif self.action in ['retrieve']:
            return [IsSuperAdmin() or IsAdmin() or IsManager() or IsMember()]  from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import User, Organization, Role
from .serializers import UserSerializer, OrganizationSerializer, RoleSerializer
from .permissions import IsSuperAdmin, IsAdmin, IsManager, IsMember, IsSuperAdminOrAdmin

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    def get_permissions(self):
        if self.action in ['create']:
            return [IsSuperAdminOrAdmin()]  # Super Admin or Admin can create organizations
        elif self.action in ['update', 'partial_update']:
            if self.request.user.is_superuser:
                return [IsSuperAdmin()]
            elif self.request.user.is_staff:  # Assuming admin users are staff
                return [IsAdmin()]
            return []  # Managers and Members cannot update
        elif self.action in ['destroy']:
            if self.request.user.is_superuser:
                return [IsSuperAdmin()]
            elif self.request.user.is_staff:  # Assuming admin users are staff
                return [IsAdmin()]
            return []  # Managers and Members cannot delete
        return super().get_permissions()

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def get_permissions(self):
        if self.action in ['create']:
            return [IsSuperAdminOrAdmin()]  # Super Admin or Admin can create roles
        elif self.action in ['update', 'partial_update']:
            if self.request.user.is_superuser:
                return [IsSuperAdmin()]
            elif self.request.user.is_staff:  # Assuming admin users are staff
                return [IsAdmin()]
            return []  # Managers and Members cannot update
        elif self.action in ['destroy']:
            if self.request.user.is_superuser:
                return [IsSuperAdmin()]
            elif self.request.user.is_staff:  # Assuming admin users are staff
                return [IsAdmin()]
            return []  # Managers and Members cannot delete
        return super().get_permissions()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['create']:
            return [IsSuperAdminOrAdmin()]  # Super Admin or Admin can create users
        elif self.action in ['update', 'partial_update']:
            if self.request.user.is_superuser:
                return [IsSuperAdmin()]
            elif self.request.user.is_staff:  # Assuming admin users are staff
                return [IsAdmin()]
            elif self.request.user.is_authenticated and self.request.user.roles.filter(name='Manager').exists():
                return [IsManager()]  # Managers can update users in their organization
            return [IsMember()]  # Members can only update their own information
        elif self.action in ['destroy']:
            if self.request.user.is_superuser:
                return [IsSuperAdmin()]
            elif self.request.user.is_staff:  # Assuming admin users are staff
                return [IsAdmin()]
            return []  # Managers and Members cannot delete users
        elif self.action in ['list']:
            if self.request.user.is_superuser:
                return [IsSuperAdmin()]
            elif self.request.user.is_staff:  # Assuming admin users are staff
                return [IsAdmin()]
            elif self.request.user.is_authenticated and self.request.user.roles.filter(name='Manager').exists():
                return [IsManager()]  # Managers can list users in their organization
            return []  # Members cannot list users
        elif self.action in ['retrieve']:
            return [IsSuperAdmin() | IsAdmin() | IsManager() | IsMember()]  # All roles can retrieve user details
        return super().get_permissions()
        return super().get_permissions()