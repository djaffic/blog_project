from django.forms import ModelForm

from .models import *


class TicketForm(ModelForm):
    """Форма обращения"""
    class Meta:
        model = Ticket
        exclude = ["created"]