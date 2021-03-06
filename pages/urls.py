from django.urls import path
from .views import *

app_name = 'pages'
urlpatterns = [
    path("", PageView.as_view(), name="page"),
    path("<slug:page>/", PageView.as_view(), name="page"),
]