from django.urls import path
from .views import cart_view
urlpatterns = [
    path('',cart_view,name='cart-page'),
] 