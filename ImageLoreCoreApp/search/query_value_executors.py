from django.contrib.auth.models import User
from ImageLoreCoreApp.models import *


def evaluate_value(value: str) -> set:
    result = set()
    is_reverse = False
    if value.startswith('!') or value.startswith('！'):
        value = value.replace('!', '').replace('！', '')
        is_reverse = True

    if value == '*':
        result = query_all()

    elif value.startswith('@'):
        value = value.replace('@', '')
        print('uploader: ', value)
        result = query_uploader(value)

    elif value.startswith('#'):
        value = value.replace('#', '')
        print('tag: ', value)
        result = query_tag(value)

    elif value.startswith('/'):
        value = value.replace('/', '')
        print('folder: ', value)
        result = query_folder(value)

    else:
        value = value.replace('#', '')
        print('implicit tag: ', value)
        result = query_tag(value)

    print('result: ', result)
    if is_reverse:
        all_image = query_all()
        result = result - all_image
        print('reversed: ', result)

    return result


def query_all():
    image_posts = ImagePost.objects.all()
    return set(image_posts.values_list('id', flat=True))


def query_uploader(username: str):
    try:
        uploader = User.objects.get(username=username)
        image_posts = ImagePost.objects.filter(uploader=uploader)
        return set(image_posts.values_list('id', flat=True))
    except User.DoesNotExist:
        return set()


def query_tag(tagname: str):
    print('    tagname: ', tagname)
    try:
        tag = Tag.objects.get(name=tagname)
        # image_posts_ids = TagPostRelation.objects.filter(tag=tag).values_list('post', flat=True)

        # queryset = ImagePost.objects.filter(id__in=image_posts_ids).order_by('-id')
        image_ids = tag.update_tag_count_recursive()
        return image_ids
    except Tag.DoesNotExist:
        raise Http404("Tag not found")


def query_folder(foldername: str):
    try:
        folder = Folder.objects.get(name=foldername)
        image_ids = folder.update_folder_count_recursive()
        return image_ids
    except Folder.DoesNotExist:
        raise Http404("Tag not found")
