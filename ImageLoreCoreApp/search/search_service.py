from ImageLoreCoreApp.search.expression_parser import ExpressionParser
from ImageLoreCoreApp.models import *


def search(expression: str):
    parser = ExpressionParser(expression)
    parser.parse()
    parser.print_tree()
    id_set = parser.evaluate()
    return ImagePost.objects.filter(id__in=id_set).order_by('-id')
