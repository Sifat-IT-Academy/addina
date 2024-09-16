from django.urls import path

from .views import *
urlpatterns = [
    path('portfolio/<int:portfolio_id>/', portfolio_detail, name='portfolio-details-page'),
    path('portfolio/',PortfolioListView.as_view(),name='portfolio-page'),
    path('portfolio/', portfolio_list_view, name='portfolio-list'),
    
]