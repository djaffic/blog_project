from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from .models import Page


class PageView(View):
    """Вывод странциы"""
    def get(self, request, page=None):
        if page is None:
            page = get_object_or_404(Page, slug__isnull=True)
        else:
            page = get_object_or_404(Page, slug=page)
        return render(request, page.template, {"page": page})