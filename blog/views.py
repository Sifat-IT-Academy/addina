from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Count
from .models import Blog, BlogCategory, BlogComment, BlogTag

class BlogListView(ListView):
    model = Blog
    context_object_name = "blogs"
    template_name = "blog.html"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = BlogTag.objects.all()  
        context['categories'] = BlogCategory.objects.all().annotate(blog_count=Count('blogs'))[:5]
        context['Blog'] = Blog.objects.all().order_by("-created_date")[:3]    
        return context


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog-details.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = self.get_object()  
        context['comments'] = BlogComment.objects.filter(blog=blog) 
        context['tags'] = BlogTag.objects.filter(blog=blog)  
        context['categories'] = BlogCategory.objects.all()
        return context
