from django.shortcuts import render

def blog_view(request):
    return render(request, "blog.html")

def blog_grid_view(request):
    return render(request, "blog-grid.html")

def blog_details_view(request):
    return render(request, "blog-details.html")
