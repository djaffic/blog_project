from django.contrib import admin
from .models import *


class TicketAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created")


admin.site.register(Ticket, TicketAdmin)
