from django.http import Http404
from rest_framework import viewsets
from rest_framework.decorators import action

from .models import Tag, TagRelation, TagAlias, Folder, FolderAlias
from .permissions import CustomPermission
from .serializers import *
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .models import ImagePost
from .serializers import ImagePostSerializer


def get_sub_tree(tag: Tag) -> {}:
    child = Tag.objects.filter(father=tag)
    child_response = []
    for tagChild in child:
        child_response.append(get_sub_tree(tagChild))
    if len(child) == 0:
        return {
            "title": tag.name,
            'value': tag.id,
            'key': tag.id,
        }
    else:
        return {
            "title": tag.name,
            'value': tag.id,
            'key': tag.id,
            'children': child_response
        }


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [CustomPermission]

    @action(detail=False, methods=['get'], url_path='trees')
    def get_whole_tree(self, request, pk=None):
        queryset = Tag.objects.filter(father=None)
        response = []
        for tag in queryset:
            response.append(get_sub_tree(tag))
        return Response(response)

    @action(detail=False, methods=['get'], url_path='roots')
    def get_root(self, request, pk=None):
        try:
            children = Tag.objects.filter(father=None)
            response = []
            if len(children) == 0:
                return Response(response)
            else:
                for tag in children:
                    is_leaf = Tag.objects.filter(father=tag).count() == 0
                    response.append({
                        "title": tag.name,
                        'value': tag.id,
                        'key': tag.id,
                        'color': tag.color,
                        'count': tag.count,
                        'isLeaf': is_leaf,
                    })
                return Response(response)

        except ImagePost.DoesNotExist:
            raise Http404("Tag not found")

    @action(detail=True, methods=['get'], url_path='children')
    def get_child(self, request, pk=None):
        try:
            instance = self.get_object()
            children = Tag.objects.filter(father=instance)
            response = []
            if len(children) == 0:
                return Response(response)
            else:
                for tag in children:
                    is_leaf = Tag.objects.filter(father=tag).count() == 0
                    response.append({
                        "title": tag.name,
                        'value': tag.id,
                        'key': tag.id,
                        'color': tag.color,
                        'count': tag.count,
                        'isLeaf': is_leaf,
                    })
                return Response(response)

        except ImagePost.DoesNotExist:
            raise Http404("Tag not found")

    @action(detail=False, methods=['get'], url_path='update-count')
    def update_count(self, request, pk=None):
        Tag.update_count()
        return Response({'message': 'success'})


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
        queryset = self.filter_queryset(self.get_queryset().order_by('-id'))

        # 使用DRF的分页
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ImagePostAllSerializer(page, many=True)
            data = serializer.data

            # 在这里可以对每个对象的数据进行处理，添加缩略图地址等信息
            for item in data:
                instance = ImagePost.objects.get(id=item['id'])
                item['image'] = instance.image.url
                item['thumbnail_small'] = instance.thumbnail_small.url if instance.thumbnail_small else None
                item['thumbnail_medium'] = instance.thumbnail_medium.url if instance.thumbnail_medium else None

            return self.get_paginated_response(data)

        # 如果没有使用分页，则直接序列化整个查询集
        serializer = ImagePostAllSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data

        # 为单个对象添加缩略图信息
        data['id'] = instance.id
        data['thumbnail_small'] = instance.thumbnail_small.url if instance.thumbnail_small else None
        data['thumbnail_medium'] = instance.thumbnail_medium.url if instance.thumbnail_medium else None

        return Response(data)

    @action(detail=True, methods=['get'], url_path='thumbnails/small')
    def get_thumbnail_small(self, request, pk=None):
        try:
            instance = self.get_object()
            if not instance.thumbnail_small:
                return Response({'error': 'No thumbnail'}, status=status.HTTP_404_NOT_FOUND)
            return Response({'thumbnail_small': instance.thumbnail_small.url if instance.thumbnail_small else None})
        except ImagePost.DoesNotExist:
            raise Http404("ImagePost not found")

    @action(detail=True, methods=['get'], url_path='tags')
    def get_tags(self, request, pk=None):
        try:
            instance = self.get_object()
            if not instance:
                return Response({'error': 'No tags'}, status=status.HTTP_404_NOT_FOUND)
            tag_set = TagPostRelation.objects.filter(post=instance)
            response = []
            for tag in tag_set:
                response.append({
                    'id': tag.tag.id,
                    'name': tag.tag.name,
                    'color': tag.tag.color,
                    'count': tag.tag.count,
                })
            return Response(response)
        except ImagePost.DoesNotExist:
            raise Http404("ImagePost not found")


class FolderView(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    permission_classes = [CustomPermission]

    @action(detail=False, methods=['get'], url_path='roots')
    def get_root(self, request, pk=None):
        try:
            children = Folder.objects.filter(father=None)
            response = []
            if len(children) == 0:
                return Response(response)
            else:
                for folder in children:
                    is_leaf = Folder.objects.filter(father=folder).count() == 0
                    response.append({
                        "title": folder.name,
                        'value': folder.id,
                        'key': folder.id,
                        'color': folder.color,
                        'isLeaf': is_leaf,
                    })
                return Response(response)

        except ImagePost.DoesNotExist:
            raise Http404("Tag not found")

    @action(detail=True, methods=['get'], url_path='children')
    def get_child(self, request, pk=None):
        try:
            instance = self.get_object()
            children = Folder.objects.filter(father=instance)
            response = []
            if len(children) == 0:
                return Response(response)
            else:
                for folder in children:
                    is_leaf = Folder.objects.filter(father=folder).count() == 0
                    response.append({
                        "title": folder.name,
                        'value': folder.id,
                        'key': folder.id,
                        'color': folder.color,
                        'isLeaf': is_leaf,
                    })
                return Response(response)
        except ImagePost.DoesNotExist:
            raise Http404("ImagePost not found")


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
