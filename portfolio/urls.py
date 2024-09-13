from django.urls import path

from .views import portfolio_details_view, portfolio_view

urlpatterns = [
    path('portfolio-details/',portfolio_details_view,name='portfolio-details-page'),
    path('portfolio/',portfolio_view,name='portfolio-page'),
    
]