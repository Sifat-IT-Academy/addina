from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import blog_details_view, blog_grid_view, blog_view

urlpatterns = [
    path('blog-details/',blog_details_view,name='blog-details-page'),
    path('blog-grid/',blog_grid_view,name='blog-grid-page'),
    path('blog/',blog_view,name='blog-page'),
]