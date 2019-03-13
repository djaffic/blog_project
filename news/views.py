from datetime import datetime

from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView

from .models import *
from .forms import CommentForm


class PostList(ListView):
    """Получаем списка статей и передаем их в шаблон"""
    context_object_name = "posts"

    def get_queryset(self):
        if self.kwargs.get('category') is not None:
            post_list = Post.objects.filter(
                category__slug=self.kwargs.get('category'),
                published=True,
                pub_date__lte=datetime.now(),
            )
            if self.request.user.is_authenticated:
                posts = post_list
            else:
                posts = post_list.filter(is_private=False)

            if posts.exists():
                self.paginate_by = posts.first().category.pagination
                self.template_name = posts.first().category.template_name
        else:
            posts = Post.objects.all()
            self.paginate_by = 5
            self.template_name = 'news/post-list.html'
        return posts


class PostDetail(DetailView):
    """Вывод одной статьи в шаблон"""
    model = Post
    template_name = "news/post-detail.html"
    # context_object_name = "post"

    # def get_queryset(self):
    #     post = Post.objects.get(
    #             category__slug=self.kwargs.get('category'),
    #             slug=self.kwargs.get('slug'),
    #             published=True,
    #             pub_date__lte=datetime.now(),
    #         )
    #     return post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

    def post(self, request, slug):
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post = Post.objects.get(slug=slug)
            form.save()
            return redirect("post_list_url")
        else:
            return HttpResponse(status=400)