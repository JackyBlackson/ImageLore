from django.shortcuts import render, get_object_or_404

from ImageLoreCoreApp.models import *


# Create your views here.
def index(request):
    return render(request, 'index.html')


def post_detail(request, id):
    # 使用get_object_or_404快捷函数来获取ImagePost对象，如果不存在则返回404错误
    post = get_object_or_404(ImagePost, pk=id)

    # 将ImagePost对象传递到模板中，并渲染页面
    return render(request, 'post/image-post/detail.html', {'image': post})


def front_page(request):
    return render(request, 'front.html', {
        'image_set': ImagePost.objects.all().order_by('-id')[:20]
    })
