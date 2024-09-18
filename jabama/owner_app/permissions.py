from rest_framework.permissions import BasePermission
from .models import Owner

class IsOwner(BasePermission):
    def has_permission(self, request, view):
        try:
            Owner.objects.get(user = request.user)
            return True
        except:
            return False
