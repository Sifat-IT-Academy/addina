from django.urls import path
from .views import CartListView
urlpatterns = [
    path('',CartListView.as_view(),name='cart-page'),
] 