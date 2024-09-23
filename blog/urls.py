from django.urls import path
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-page'),
    path('category/<int:category_id>/', BlogListView.as_view(), name='blog-page'),
    path('tag/<int:tag_id>/', BlogListView.as_view(), name='blogs_by_tag'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
=======
from .views import BlogDetailView,BlogListView

urlpatterns = [
    path('blog-details/<int:pk>/',BlogDetailView.as_view(),name='blog-details-page'),
    path('',BlogListView.as_view(),name='blog-page'),
>>>>>>> e5d73b4daed339bb46d08ce6eb21aea8ca1248e4
]