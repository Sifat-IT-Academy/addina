from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import BlogListView,Blog_detailsListView

urlpatterns = [
    path('category/<int:category_id>/', BlogListView.as_view(), name='blog-page'),
    path('tag/<int:tag_id>/', BlogListView.as_view(), name='blogs_by_tag'),
    path('blog-details/',Blog_detailsListView.as_view(),name='blog-details-page'),
    path('blog/',BlogListView.as_view(),name='blog-page'),

]