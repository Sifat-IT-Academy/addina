from django.urls import path
from .views import PortfolioDetailsListView, PortfolioListView

urlpatterns = [
    path('portfolio-details/<int:id>/', PortfolioDetailsListView.as_view(), name='portfolio-details-page'),
    path('portfolio/', PortfolioListView.as_view(), name='portfolio-page'),
]
