from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views import View

from .models import *
from .forms import CommentForm


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
        form = CommentForm()
        return render(request, "news/post-detail.html", {"post": post, "form": form})

    def post(self, request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post = Post.objects.get(id=pk)
            form.save()
            return redirect("post_list_url")
        else:
            return HttpResponse(status=404)