from django.urls import path
from .views import *

urlpatterns = [
    path('', PostList.as_view(), name="post_list_url"),
    path("search/", Search.as_view(), name='search_form_url'),
    path("filter/<int:pk>", DateFilter.as_view(), name='date_filter_url'),
    path("<slug:category>/", PostList.as_view(), name='post_by_category_url'),
    path("<slug:category>/<slug:slug>/", PostDetail.as_view(), name='post_detail_url'),
]