from rest_framework import permissions

class CanViewFinance(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('finance.view_finance_section')
    
class CanEditFinance(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('finance.edit_finance_section')
