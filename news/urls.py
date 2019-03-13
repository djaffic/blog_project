from django.urls import path
from .views import *

urlpatterns = [
    path('', PostList.as_view(), name="post_list_url"),
    path("<slug:category>/", PostList.as_view(), name='post_by_category_url'),
    path("<slug:category>/<slug:slug>/", PostDetail.as_view(), name='post_detail_url'),
]