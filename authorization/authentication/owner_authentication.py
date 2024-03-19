from rest_framework import status
from authorization.models import User
from rest_framework.response import Response
from rest_framework.permissions import BasePermission


class OwnerIsAuthenticated(BasePermission):
    """
    Custom class for Authentication specific only for owners.
    """
    def has_permission(self, request, view):
        try:
            user = User.objects.get(email=request.user)
            return bool(request.user and request.user.is_authenticated and user.is_owner)

        except Exception:
            return False


class TenantIsAuthenticated(BasePermission):
    """
    Custom class for Authentication specific only for tenants.
    """
    def has_permission(self, request, view):
        try:
            user = User.objects.get(email=request.user)
            return bool(request.user and request.user.is_authenticated and not user.is_owner)

        except Exception:
            return False
