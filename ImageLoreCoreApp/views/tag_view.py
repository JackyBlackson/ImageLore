from django.http import Http404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ImageLoreCoreApp.models import Tag, ImagePost
from ImageLoreCoreApp.permissions import CustomPermission
from ImageLoreCoreApp.serializers import TagSerializer
from ImageLoreCoreApp.models import TagAlias
from ImageLoreCoreApp.models import TagRelation
from ImageLoreCoreApp.models import TagPostRelation
from ImageLoreCoreApp.serializers import ImagePostSerializer, ImagePostAllSerializer
from ImageLoreCoreApp.search.search_service import search


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [CustomPermission]

    @action(detail=False, methods=['get'], url_path='simple')
    def tags(self, request):
        instances = Tag.objects.all()
        data = []
        for instance in instances:
            data.append({
                "id": instance.id,
                'name': instance.name,
                'color': instance.color,
                'count': instance.count,
                'contribute': instance.contribute
            })
        return Response(data)

    @action(detail=True, methods=['get'], url_path='images')
    def list_images(self, request, pk=None):
        try:
            tag = self.get_object()
            # image_posts_ids = TagPostRelation.objects.filter(tag=tag).values_list('post', flat=True)


            # queryset = ImagePost.objects.filter(id__in=image_posts_ids).order_by('-id')
            image_ids = tag.update_tag_count_recursive()
            queryset = search(f'#{tag.name}')
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
        except Tag.DoesNotExist:
            raise Http404("Tag not found")

    @action(detail=False, methods=['get'], url_path='trees')
    def get_whole_tree(self, request, pk=None):
        queryset = Tag.objects.filter(father=None)
        response = []
        for tag in queryset:
            response.append(get_sub_tree(tag))
        return Response(response)

    @action(detail=False, methods=['get'], url_path='relations')
    def get_relations(self, request, pk=None):
        queryset = self.get_queryset()
        response = {
            'strong': [],
            'tag_list': [],
            'primary': [],
            'secondary': []
        }
        for tag in queryset:
            response['tag_list'].append(tag.to_json())
            if tag.father is None:
                response['strong'].append(tag.to_json())
            else:
                response['primary'].append({
                    'father': tag.father.to_json(),
                    'child': tag.to_json()
                })
        relation_set = TagRelation.objects.all()
        for relation in relation_set:
            response['secondary'].append({
                'description': relation.description,
                'father': relation.father_tag.to_json(),
                'child': relation.child_tag.to_json()})
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
