from django.shortcuts import render

def index_view(request):
    return render(request, "index.html")

def product_view(request):
    return render(request, "product.html")

def product_details_view(request):
    return render(request, "product-details.html")

