from django.urls import path

from.views import contact

urlpatterns = [
    path('', contact, name='contact'),
    path('thanks/', contact, name='thanks'),
]