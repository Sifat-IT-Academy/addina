from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-page'),
    path('category/<int:category_id>/', BlogListView.as_view(), name='blog-page'),
    path('tag/<int:tag_id>/', BlogListView.as_view(), name='blogs_by_tag'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
]