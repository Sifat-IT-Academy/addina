from django.urls import path
from .views import cart,sub_cart,add_cart,remove_cart

urlpatterns = [
    path('', cart, name="cart"),
    path('add_product/<int:product_id>/', add_cart, name="add-from-cart"),
    path('sub_product/<int:product_id>/', sub_cart, name="sub-cart"),
    path('remove_product/<int:product_id>/', remove_cart, name="remove-cart"),
]
