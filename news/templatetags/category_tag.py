from django import template

from news.models import Category


register = template.Library()


@register.inclusion_tag("tags/category-list.html")
def category_list():
    return {"categories": Category.objects.all()}