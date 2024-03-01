from rest_framework import serializers
from django.contrib.auth.models import User, Permission


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # 定义需要序列化的字段


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'name', 'content_type', ...]  # 定义需要序列化的字段
