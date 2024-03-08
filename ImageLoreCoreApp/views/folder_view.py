from django.http import Http404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ImageLoreCoreApp.models import Folder, ImagePost
from ImageLoreCoreApp.permissions import CustomPermission
from ImageLoreCoreApp.serializers import FolderSerializer


class FolderView(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    permission_classes = [CustomPermission]

    @action(detail=False, methods=['get'], url_path='simple')
    def folders(self, request):
        queryset = Folder.objects.all()
        data = []
        for folder in queryset:
            data.append({
                "id": folder.id,
                'name': folder.name,
                'color': folder.color,
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
                    count = ImagePost.objects.filter(folder=folder).count()
                    response.append({
                        "title": folder.name,
                        'value': folder.id,
                        'key': folder.id,
                        'color': folder.color,
                        'isLeaf': is_leaf,
                        'count': count,
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
