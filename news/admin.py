from mptt.admin import MPTTModelAdmin
from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import *


admin.site.site_title = "Проект блога"
admin.site.site_header = "Проект блога"


class CommentAdmin(admin.StackedInline):
    """Комментарии"""
    model = Comment
    extra = 1
    # max_num = 100
    list_display = ("id", "post", "moderation")
    list_display_links = ("post",)
    list_editable = ("moderation",)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Статьи"""
    list_display = ("id", "title", "pub_date")
    prepopulated_fields = {'slug':("title",)}
    list_display_links = ("title",)
    search_fields = ("title", "text",)
    list_filter = ("created", "updated", "pub_date", "published", "category")
    list_per_page = 20
    inlines = [CommentAdmin]
    actions_on_bottom = True
    actions_on_top = False
    # fieldsets = (
    #     (None, {
    #         'fields': ('title', 'text')
    #     }),
    #     ("Категории/Теги", {
    #         'classes': ('collapse',),
    #         'fields': ('category', 'tags')
    #     }),
    # )
    # filter_horizontal = ("tags",)
    # filter_vertical = ("tags",)/

@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    """Категории"""
    prepopulated_fields = {'slug':("name",)}
    mptt_level_indent = 20

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Теги"""
    prepopulated_fields = {'slug':("name",)}


admin.site.register(Comment)
admin.site.unregister(User)
admin.site.unregister(Group)
