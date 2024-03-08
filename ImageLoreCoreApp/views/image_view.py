from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from ImageLoreCoreApp.models import ImagePost, TagPostRelation
from ImageLoreCoreApp.permissions import CustomPermission
from ImageLoreCoreApp.serializers import ImagePostSerializer, ImagePostAllSerializer

from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from ImageLoreCoreApp.models import ImagePost, TagPostRelation
from ImageLoreCoreApp.permissions import CustomPermission
from ImageLoreCoreApp.serializers import ImagePostSerializer, ImagePostAllSerializer
from ImageLoreCoreApp.search.search_service import search
import traceback


class ImagePostView(viewsets.ModelViewSet):
    queryset = ImagePost.objects.all()
    serializer_class = ImagePostSerializer
    permission_classes = [CustomPermission]

    @action(detail=False, methods=['get'], url_path='search')
    def search(self, request, *args, **kwargs):
        expression = request.GET.get('expr')

        if not expression:
            expression = ''

        print('expression: ', expression)

        try:
            queryset = search(expression)  # Assuming search(expression) returns the desired queryset

            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = ImagePostAllSerializer(page, many=True)
                data = serializer.data

                # 对每个对象的数据进行处理，添加图片和缩略图地址等信息
                for item in data:
                    instance = ImagePost.objects.get(id=item['id'])
                    item['image'] = instance.image.url
                    item['thumbnail_small'] = instance.thumbnail_small.url if instance.thumbnail_small else None
                    item['thumbnail_medium'] = instance.thumbnail_medium.url if instance.thumbnail_medium else None
                print('response: ', self.get_paginated_response(data))
                return self.get_paginated_response(data)

            serializer = ImagePostAllSerializer(queryset, many=True)

            return Response(serializer.data)
        except Exception as e:
            traceback.print_exc()
            return Response(str(e), status=500)

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
