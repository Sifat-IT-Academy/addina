from django.urls import path
from .views import CartListView, remove_from_cart

urlpatterns = [
    path('', CartListView.as_view(), name='cart-page'),  # Cart sahifasi
    path('remove/<int:cart_id>/', remove_from_cart, name='remove-from-cart'),  # Mahsulotni o'chirish sahifasi
]
