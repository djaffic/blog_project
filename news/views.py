from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView

from .models import *
from .forms import CommentForm


class PostList(ListView):
    """Получаем списка статей и передаем их в шаблон"""
    model = Post
    context_object_name = "posts"
    queryset = Post.objects.filter(published=True)
    print(queryset)
    template_name = "news/post-list.html"


    # def get(self, request, slug=None):
    #     if slug is not None:
    #         posts = get_list_or_404(Post, category__slug=slug)
    #     else:
    #         posts = Post.objects.all()
    #     return render(request, "news/post-list.html", {'posts': posts})


class PostDetail(DetailView):
    """Вывод одной статьи в шаблон"""
    model = Post
    template_name = "news/post-detail.html"
    # context_object_name = "post"

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