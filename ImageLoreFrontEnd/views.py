from django.shortcuts import render, get_object_or_404

from ImageLoreCoreApp.models import *


# Create your views here


def post_detail(request, id):
    # 使用get_object_or_404快捷函数来获取ImagePost对象，如果不存在则返回404错误
    post = get_object_or_404(ImagePost, pk=id)
    tag_set = TagPostRelation.objects.filter(post=post)

    # 将ImagePost对象传递到模板中，并渲染页面
    return render(request, 'post/detail.html',
                  {
                      'image': post,
                      'tag_set': tag_set,
                  })


def front_page(request):
    image_set = ImagePost.objects.all().order_by('-id')[:20]
    tag_set = get_whole_tree()
    tag_count = len(Tag.objects.all())
    return render(request, 'front.html', {
        'image_set': image_set,
        'tag_set': tag_set,
        'tag_count': tag_count
    })
