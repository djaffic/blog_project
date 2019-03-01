from django.urls import path
from .views import *

urlpatterns = [
    path('', PostList.as_view(), name="post_list_url"),
    path('category/<slug:slug>/', PostList.as_view(), name='post_by_category_url'),
    path('comment/<int:pk>/', PostDetail.as_view(), name='add_comment_url'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail_url'),
]