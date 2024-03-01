"""
URL configuration for ImageLore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from ImageLore import settings
from UserAndPermission.api.views import UserViewSet, PermissionViewSet
from ImageLoreCoreApp.views import *
from django.conf.urls.static import static

from ImageLoreFrontEnd.views import *

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'permissions', PermissionViewSet)

router.register(r'tag', TagViewSet)
router.register(r'alias/tag', TagAliasViewSet)

router.register(r'tag/relation/tag', TagRelationViewSet)
router.register(r'tag/relation/post', TagPostRelationViewSet)
router.register(r'tag/relation/folder', TagFolderRelationViewSet)

router.register(r'folder', FolderView)
router.register(r'alias/folder', FolderAliasView)

router.register(r'post/image', ImagePostView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include(router.urls)),
    path('', index, name='index'),
]


if settings.USE_DJANGO_STATIC_FILE_SERVICE:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)