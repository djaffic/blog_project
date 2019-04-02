from django.contrib import admin
from .models import UserProfile

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Регистрация профилей в админке"""
    list_display = ("user", "age", "gender")
    list_display_links = ("user", )