from rest_framework import permissions


# Разрешение, позволяющее изменять данные только текущему владельцу.
class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user
