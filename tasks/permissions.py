from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsProjectMemberOrAdmin(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return True

    def has_object_permission(self, request, view, obj):
        user = request.user

        if request.method in SAFE_METHODS:
            return True

        if user.role in ['a', 'sa']:
            return True

        return user in obj.users.all()
