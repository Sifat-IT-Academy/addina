from django.urls import path
from .views import index_view, product_view, product_details_view

urlpatterns = [
    path('',index_view,name='home-page'),
    path('product/',product_view,name='product-page'),
    path('product-details/',product_details_view,name='product-details-page'),
]
