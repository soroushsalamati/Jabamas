from rest_framework.permissions import BasePermission
from .models import Customer

class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        try:
            Customer.objects.get(user = request.user)
            return True
        except:
            return False