from rest_framework import viewsets
from .models import Tag, TagRelation, TagAlias, Folder, FolderAlias
from .permissions import CustomPermission
from .serializers import *
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .models import ImagePost
from .serializers import ImagePostSerializer



class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [CustomPermission]


class TagRelationViewSet(viewsets.ModelViewSet):
    queryset = TagRelation.objects.all()
    serializer_class = TagRelationSerializer
    permission_classes = [CustomPermission]


class TagAliasViewSet(viewsets.ModelViewSet):
    queryset = TagAlias.objects.all()
    serializer_class = TagAliasSerializer
    permission_classes = [CustomPermission]


class ImagePostView(viewsets.ModelViewSet):
    queryset = ImagePost.objects.all()
    serializer_class = ImagePostSerializer
    permission_classes = [CustomPermission]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = ImagePostAllSerializer(queryset, many=True)
        data = serializer.data

        # 在这里可以对每个对象的数据进行处理，添加缩略图地址等信息
        for item in data:
            instance = ImagePost.objects.get(id=item['id'])
            item['thumbnail_small'] = instance.thumbnail_small.url if instance.thumbnail_small else None
            item['thumbnail_medium'] = instance.thumbnail_medium.url if instance.thumbnail_medium else None

        return Response(data)




class FolderView(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
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

