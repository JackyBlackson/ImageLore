from rest_framework import viewsets

from .permissions import CustomPermission
from .serializers import *


class TagRelationViewSet(viewsets.ModelViewSet):
    queryset = TagRelation.objects.all()
    serializer_class = TagRelationSerializer
    permission_classes = [CustomPermission]


class TagAliasViewSet(viewsets.ModelViewSet):
    queryset = TagAlias.objects.all()
    serializer_class = TagAliasSerializer
    permission_classes = [CustomPermission]


class FolderAliasView(viewsets.ModelViewSet):
    queryset = FolderAlias.objects.all()
    serializer_class = FolderAliasSerializer
    permission_classes = [CustomPermission]


class TagFolderRelationViewSet(viewsets.ModelViewSet):
    queryset = TagFolderRelation.objects.all()
    serializer_class = TagFolderRelationSerializer
    permission_classes = [CustomPermission]


class TagPostRelationViewSet(viewsets.ModelViewSet):
    queryset = TagPostRelation.objects.all()
    serializer_class = TagPostRelationSerializer
    permission_classes = [CustomPermission]
