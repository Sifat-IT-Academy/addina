from django.urls import path
from .views import BlogDetailView,BlogListView

urlpatterns = [
    path('blog-details/<int:pk>/',BlogDetailView.as_view(),name='blog-details-page'),
    path('',BlogListView.as_view(),name='blog-page'),
]