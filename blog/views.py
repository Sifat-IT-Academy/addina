from django.shortcuts import render
from django.views.generic import ListView
from .models import Blog,BlogCategory,BlogComment,BlogTag,Blog_details

class BlogListView(ListView):
    model = Blog
    context_object_name = "blogs"
    template_name = "blog.html"
    paginate_by = 2 
    
class Blog_detailsListView(ListView):
    model = Blog_details
    context_object_name = 'blog_details'
    template_name = 'blog-details.html'