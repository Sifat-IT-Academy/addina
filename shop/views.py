from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, ProductComment
from .forms import ProductCommentForm

def index_view(request):
    return render(request, "index.html")

def about_view(request):
    return render(request, 'about.html')

def wishlist_view(request):
    return render(request, 'wishlist.html')

class ProductListView(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'products'
    paginate_by = 3




def product_details_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    comments = product.productcomment_set.all()
    comment_count = comments.count()   
    

    if request.method == 'POST':
        form = ProductCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            # comment.user = request.user
            comment.save()
            return redirect('product-details-page', product_id=product.id)
    else:
        form = ProductCommentForm()

    return render(request, 'product-details.html', {
        'product': product,
        'comments': comments,
        'comment_count': comment_count,
        'form': form,
        'ratings_range': range(1, 6) 
    })