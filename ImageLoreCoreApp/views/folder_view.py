from django.http import Http404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ImageLoreCoreApp.models import Folder, ImagePost
from ImageLoreCoreApp.permissions import CustomPermission
from ImageLoreCoreApp.serializers import FolderSerializer
from ImageLoreCoreApp.search.search_service import search
from ImageLoreCoreApp.models import Tag, ImagePost
from ImageLoreCoreApp.permissions import CustomPermission
from ImageLoreCoreApp.serializers import TagSerializer
from ImageLoreCoreApp.models import TagAlias
from ImageLoreCoreApp.models import TagRelation
from ImageLoreCoreApp.models import TagPostRelation
from ImageLoreCoreApp.serializers import ImagePostSerializer, ImagePostAllSerializer


class FolderView(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    permission_classes = [CustomPermission]

    @action(detail=False, methods=['get'], url_path='trees')
    def get_whole_tree(self, request, pk=None):
        queryset = Folder.objects.filter(father=None)
        response = []
        for folder in queryset:
            response.append(get_sub_tree(folder))
        return Response(response)

    @action(detail=False, methods=['get'], url_path='simple')
    def folders(self, request):
        queryset = Folder.objects.all()
        data = []
        for folder in queryset:
            is_leaf = Folder.objects.filter(father=folder).count() == 0
            data.append({
                "id": folder.id,
                'name': folder.name,
                'color': folder.color,
                'isLeaf': is_leaf,
                'count': folder.count,
            })
        return Response(data)

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
                        'count': folder.count,
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
                        'count': folder.count,
                    })
                return Response(response)
        except ImagePost.DoesNotExist:
            raise Http404("ImagePost not found")

    @action(detail=False, methods=['get'], url_path='update-count')
    def update_count(self, request, pk=None):
        Folder.update_count()
        return Response({'message': 'success'})

    @action(detail=True, methods=['get'], url_path='images')
    def list_images(self, request, pk=None):
        try:
            folder = self.get_object()
            # image_posts_ids = TagPostRelation.objects.filter(tag=tag).values_list('post', flat=True)

            # queryset = ImagePost.objects.filter(id__in=image_posts_ids).order_by('-id')
            queryset = search(f'/{folder.name}')
            # 使用DRF的分页
            page = (self.paginate_queryset(queryset))
            if page is not None:
                serializer = ImagePostAllSerializer(page, many=True)
                data = serializer.data

                # 对每个对象的数据进行处理，添加图片和缩略图地址等信息
                for item in data:
                    instance = ImagePost.objects.get(id=item['id'])
                    item['image'] = instance.image.url
                    item['thumbnail_small'] = instance.thumbnail_small.url if instance.thumbnail_small else None
                    item['thumbnail_medium'] = instance.thumbnail_medium.url if instance.thumbnail_medium else None

                return self.get_paginated_response(data)

            # 如果没有使用分页，则直接序列化整个查询集
            serializer = ImagePostAllSerializer(queryset, many=True)
            return Response(serializer.data)
        except Folder.DoesNotExist:
            raise Http404("Tag not found")

    @action(detail=False, methods=['get'], url_path='relations')
    def get_relations(self, request, pk=None):
        queryset = self.get_queryset()
        response = {
            'folder_list': [],
            'primary': [],
            'secondary': [],
            'strong': []
        }
        for folder in queryset:
            response['folder_list'].append(folder.to_json())
            if folder.father is None:
                response['strong'].append(folder.to_json())
            else:
                response['primary'].append({
                    'father': folder.father.to_json(),
                    'child': folder.to_json()
                })
        return Response(response)


def get_sub_tree(tag: Folder) -> {}:
    child = Folder.objects.filter(father=tag)
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

