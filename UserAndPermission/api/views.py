from rest_framework import viewsets
from django.contrib.auth.models import User, Permission
from rest_framework.decorators import action
from rest_framework.response import Response

from ImageLoreCoreApp.models import ImagePost
from .serializer import UserSerializer, PermissionSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'], url_path='simple')
    def users(self, request):
        queryset = User.objects.all()
        data = []
        for user in queryset:
            count = ImagePost.objects.filter(uploader=user).count()
            data.append({
                'id': user.id,
                'name': user.username,
                'email': user.email,
                'count': count,
            })
        return Response(data)


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
