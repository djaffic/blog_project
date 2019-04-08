from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import TicketForm


class TicketsListView(ListView):
    """список тикетов"""
    model = Ticket
    template_name = "tickets/tickets-list.html"
    context_object_name = "tickets"


class TicketCreateView(CreateView):
    """создание тикета"""
    model = Ticket
    form_class = TicketForm
    template_name = "tickets/ticket-form.html"


class TicketUpdateView(UpdateView):
    """Редактирование тикета"""
    model = Ticket
    form_class = TicketForm
    template_name = "tickets/ticket-form.html"


class TicketDeleteView(DeleteView):
    """Удаление тикета"""
    model = Ticket
    template_name = "tickets/ticket_confirm_delete.html"
    success_url = reverse_lazy("tickets_list_url")