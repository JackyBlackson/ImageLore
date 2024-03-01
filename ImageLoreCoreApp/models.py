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

    def __str__(self):
        return f"[{self.id}]{self.name}"


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
