from django.contrib import admin
from .models import Page


class PageAdmin(admin.ModelAdmin):
    """Админика страницы"""
    list_display = ("title", "id")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Page, PageAdmin)
