import ImageLore.site_config as config


def custom_context(request):
    # 定义你想要添加到模板上下文的全局变量
    custom_context = {
        'site_host' : config.SITE_HOST,
        'root_url': config.ROOT_URL,
        'site_title': config.SITE_TITLE,
        # 其他全局变量
    }
    return custom_context