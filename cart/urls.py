from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import cart_view
urlpatterns = [
    path('cart/',cart_view,name='cart-page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)