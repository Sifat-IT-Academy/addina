from django.urls import path

<<<<<<< HEAD
from .views import *
urlpatterns = [
    path('portfolio/<int:portfolio_id>/', portfolio_detail, name='portfolio-details-page'),
    path('portfolio/',PortfolioListView.as_view(),name='portfolio-page'),
    path('portfolio/', portfolio_list_view, name='portfolio-list'),
=======
from .views import portfolio_details_view,PortfolioListView

urlpatterns = [
    path('portfolio-details/',portfolio_details_view,name='portfolio-details-page'),
    path('',PortfolioListView.as_view(),name='portfolio-page'),
>>>>>>> e5d73b4daed339bb46d08ce6eb21aea8ca1248e4
    
]