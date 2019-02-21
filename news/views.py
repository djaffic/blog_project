from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import *


class PostList(View):
    """Получаем списка статей и передаем их в шаблон"""
    def get(self, request):
        posts = Post.objects.all()
        category = Category.objects.all()
        context = {
            'posts': posts,
            'category': category
        }
        return render(request, "news/post-list.html", context)


class CategoryList(View):
    """Вывод списка категорий"""
    def get(self, request):
        categories = Category.objects.all()
        return render(request, "news/category-list.html", {"categories": categories})


class PostDetail(View):
    """Вывод одной статьи в шаблон"""
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, "news/post-detail.html", {"post": post})


class PostsByCategory(View):
    """Вывод статей по категориям"""
    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        posts = Post.objects.filter(category=category)
        return render(request, "news/posts-by-category.html", {"posts": posts, "category": category})