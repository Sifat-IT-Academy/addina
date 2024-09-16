from django.urls import path

from .views import portfolio_details_view,PortfolioListView

urlpatterns = [
    path('portfolio-details/',portfolio_details_view,name='portfolio-details-page'),
    path('',PortfolioListView.as_view(),name='portfolio-page'),
    
]