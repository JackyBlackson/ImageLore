from rest_framework import permissions


class CustomPermission(permissions.IsAuthenticatedOrReadOnly):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        # 您可以根据需要定义其他自定义权限规则
        return True
