from django.contrib import admin
from .models import Page


class PageAdmin(admin.ModelAdmin):
    """Админика страницы"""
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Page, PageAdmin)
