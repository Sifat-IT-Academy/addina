from django.shortcuts import render
from django.views.generic import ListView
from .models import Blog,BlogCategory,BlogComment,BlogTag

class BlogListView(ListView):
    model = Blog
    context_object_name = "blogs"
    template_name = "blog.html"


def blog_grid_view(request):
    return render(request, "blog-grid.html")

def blog_details_view(request):
    return render(request, "blog-details.html")
