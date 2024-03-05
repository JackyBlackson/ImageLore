from django.contrib.auth.models import User
from django.db import models
import hashlib
from datetime import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# 标签类


class Tag(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    # fullname = models.CharField(max_length=255, unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    IMG_ONLY = 1
    FOLDER_ONLY = 2
    BOTH = 3
    TYPE_CHOICES = [
        (IMG_ONLY, 'img_only'),
        (FOLDER_ONLY, 'folder_only'),
        (BOTH, 'both'),
    ]
    type = models.IntegerField(choices=TYPE_CHOICES, default=BOTH)
    color = models.CharField(max_length=8, default="#000000")
    father = models.ForeignKey('self', related_name='tagtree', null=True, blank=True, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

    prefix = "%20%20"

    @staticmethod
    def update_count():
        # 获取所有根节点tags
        root_tags = Tag.objects.filter(father__isnull=True)

        for root_tag in root_tags:
            # 更新每个根节点下的tags的count
            Tag._update_tag_count_recursive(root_tag)

    @staticmethod
    def _update_tag_count_recursive(tag):
        # 获取当前tag直接标记的图片
        direct_images = set(tag.tag_post_relations_tag.values_list('post', flat=True))

        # 获取子tags
        child_tags = tag.tagtree.all()
        all_images = direct_images.copy()

        for child_tag in child_tags:
            # 递归获取子tag的所有图片（包括其子tag标记的图片）
            child_images = Tag._update_tag_count_recursive(child_tag)
            # 合并图片集合，排除重复项
            all_images |= child_images

        # 更新当前tag的count
        tag.count = len(all_images)
        tag.save()

        return all_images

    def __str__(self):
        return f"[{self.id}]{self.name}"


PREFIX = f"%20%20"

def __get_sub_tree(tag, layer=0) -> []:
    child = Tag.objects.filter(father=tag)
    folder_count = TagFolderRelation.objects.filter(tag=tag)
    print(f'[{tag.name}]folder_count: ', folder_count)
    image_count = TagPostRelation.objects.filter(tag=tag)
    print(f'[{tag.name}]folder_count: ', image_count)
    child_response = []
    for tagChild in child:
        sub_response = __get_sub_tree(tagChild, layer + 1)
        child_response.append(sub_response)
    if len(child) == 0:
        return {
            'tag': tag,
            'depth': layer,
            'folder_count': folder_count.count(),
            'image_count': image_count.count(),
        }
    else:
        return {
            'tag': tag,
            'depth': layer,
            'folder_count': folder_count.count(),
            'image_count': image_count.count(),
            'children': child_response
        }


def get_whole_tree() -> []:
    queryset = Tag.objects.filter(father=None)
    response = []
    layer = 0
    for tag in queryset:
        response.append(__get_sub_tree(tag, layer + 1))
    print(response)
    return response


class TagRelation(models.Model):
    """
    标签和标签的父子关系
    """
    father_tag = models.ForeignKey(Tag, related_name='father_tag_relations', on_delete=models.CASCADE)
    child_tag = models.ForeignKey(Tag, related_name='child_tag_relations', on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"[{self.father_tag.id}]{self.father_tag.name} --> [{self.child_tag.id}]{self.child_tag.name}"


class TagAlias(models.Model):
    tag = models.ForeignKey(Tag, related_name='tag_aliases', on_delete=models.CASCADE)
    alias = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"[{self.tag.id}]{self.tag.name} <-- [{self.id}]{self.alias}"


class Folder(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    color = models.CharField(max_length=8, default="#000000")
    father = models.ForeignKey('self', related_name='folders', null=True, blank=True, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)



    def __str__(self):
        return self.name


class FolderAlias(models.Model):
    folder = models.ForeignKey(Folder, related_name='folder_aliases', on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True, null=True)
    alias = models.CharField(max_length=255)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"[{self.folder.id}]{self.folder.name} <-- [{self.id}]{self.alias}"


class TagFolderRelation(models.Model):
    tag = models.ForeignKey(Tag, related_name='tag_folder_relations_tag', on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, related_name='tag_folder_relations_folder', on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.folder.id}]{self.folder.name} <-- [{self.tag.id}]{self.tag.name}"


class ImagePost(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    uploader = models.ForeignKey(User, related_name='image', on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, related_name='img_in_folder', on_delete=models.CASCADE)
    color = models.CharField(max_length=8, default="#000000")
    image = models.ImageField(upload_to='images/')
    thumbnail_small = models.ImageField(upload_to='thumbnails/small/', blank=True)
    thumbnail_medium = models.ImageField(upload_to='thumbnails/medium/', blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.id}]{self.name}--{self.uploader.get_full_name()}"


class TagPostRelation(models.Model):
    post = models.ForeignKey(ImagePost, related_name='tag_post_relations_post', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, related_name='tag_post_relations_tag', on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.post.id}]{self.post.name} <-- [{self.tag.id}]{self.tag.name}"
