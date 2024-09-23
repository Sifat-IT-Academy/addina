from django.urls import path
from .views import *

urlpatterns = [
    path('',index_view,name='home-page'),
    path('about/',about_view,name='about-page'),
    path('product/',ProductListView.as_view(),name='product-page'),
    path('product/<int:product_id>/',product_details_view,name='product-details-page'),
]
