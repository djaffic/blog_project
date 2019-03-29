from django import template

from news.models import Category


register = template.Library()


@register.inclusion_tag("tags/base-tags.html")
def category_list(template="tags/category-list.html"):
    return {
        "template": template,
        "categories": Category.objects.all()
    }