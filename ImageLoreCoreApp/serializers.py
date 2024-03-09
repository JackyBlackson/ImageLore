from rest_framework import serializers
from .models import *
from PIL import Image as PILImage, UnidentifiedImageError
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework import serializers
from .models import ImagePost

from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class TagRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagRelation
        fields = '__all__'


class TagAliasSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagAlias
        fields = '__all__'


def create_thumbnail(self, image_field, size):
    try:
        img = Image.open(image_field)
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, format='PNG', quality=90)  # 保存为JPEG格式，可以根据需要修改格式和质量

        thumbnail = InMemoryUploadedFile(thumb_io, None, image_field.name, 'image/png',
                                         thumb_io.tell, None)
        return thumbnail
    except UnidentifiedImageError:
        # 如果无法识别图片格式，则做相应处理
        # 这里可以返回错误信息或者采取其他操作
        return None


class ImagePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagePost
        fields = ['uploader', 'name', 'description', 'folder', 'color', 'image']

    def create(self, validated_data):
        image = validated_data.pop('image')
        validated_data['image'] = image

        instance = super().create(validated_data)
        small_thumbnail = create_thumbnail(self, image, (100, 100))
        medium_thumbnail = create_thumbnail(self, image, (300, 300))

        instance.thumbnail_small.save(f"{instance.id}.jpg", small_thumbnail)
        instance.thumbnail_medium.save(f"{instance.id}.jpg", medium_thumbnail)

        return instance


class ImagePostAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagePost
        fields = '__all__'


class TagPostRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagPostRelation
        fields = '__all__'


class TagFolderRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagFolderRelation
        fields = '__all__'


class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = '__all__'


class FolderAliasSerializer(serializers.ModelSerializer):
    class Meta:
        model = FolderAlias
        fields = '__all__'



