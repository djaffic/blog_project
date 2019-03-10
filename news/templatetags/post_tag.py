from django import template

from news.models import Post


register = template.Library()


@register.inclusion_tag("tags/base_tags.html")
def post_list(template="tags/post-list.html"):
    return {
        "template": template,
        "posts": Post.objects.all()[:5]
    }