from django.urls import path
from .views import *

urlpatterns = [
    path('', PostList.as_view(), name="post_list_url"),
    path('categories/', CategoryList.as_view(), name="categories_list_url"),
    path('<int:pk>', PostDetail.as_view(), name='post_detail_url'),
    path('<slug:slug>', PostsByCategory.as_view(), name='post_by_category_url'),
]