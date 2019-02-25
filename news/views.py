from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import View
from .forms import CommentForm

from .models import *


class PostList(View):
    """Получаем списка статей и передаем их в шаблон"""

    def get(self, request, slug=None):
        if slug is not None:
            posts = get_list_or_404(Post, category__slug=slug)
        else:
            posts = Post.objects.all()
        return render(request, "news/post-list.html", {'posts': posts})


class PostDetail(View):
    """Вывод одной статьи в шаблон"""

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        return render(request, "news/post-detail.html", {"post": post})