from django.urls import path
from .views import *

urlpatterns = [
    path('', TicketsListView.as_view(), name='tickets_list_url'),
    path('add/', TicketCreateView.as_view(), name='ticket_create_url'),
    path('update/<int:pk>/', TicketUpdateView.as_view(), name='ticket_update_url'),
    path('delete/<int:pk>/', TicketDeleteView.as_view(), name='ticket_delete_url'),
]