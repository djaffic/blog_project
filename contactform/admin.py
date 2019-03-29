from django.contrib import admin

from .models import Contact

# @admin.register(Contact)
# class ContactAdmin(admin.ModelAdmin):
#     list_display = ("last_name", "first_name", "email")
#     list_display_links = ("last_name",)

admin.site.register(Contact)