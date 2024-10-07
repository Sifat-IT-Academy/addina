from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import BlogListView,Blog_detailsListView

urlpatterns = [
<<<<<<< HEAD
    path('', BlogListView.as_view(), name='blog-page'),
    path('category/<int:category_id>/', BlogListView.as_view(), name='blog-page'),
    path('tag/<int:tag_id>/', BlogListView.as_view(), name='blogs_by_tag'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
=======
    path('blog-details/',Blog_detailsListView.as_view(),name='blog-details-page'),
    path('blog/',BlogListView.as_view(),name='blog-page'),
>>>>>>> ffa80903c789f0f2e8c562fbbadaa7aa4cd6a0a2
]