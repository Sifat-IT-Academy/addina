from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import portfolio_details_view, portfolio_view

urlpatterns = [
    path('portfolio-details/',portfolio_details_view,name='portfolio-details-page'),
    path('portfolio/',portfolio_view,name='portfolio-page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)