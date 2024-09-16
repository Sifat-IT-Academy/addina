from django.shortcuts import render
from django.views.generic import ListView
from .models import Portfolio,Portfolio_details

class PortfolioListView(ListView):
    model = Portfolio
    context_object_name = "portfolio"
    template_name = "portfolio.html"
class PortfolioDetailsListView(ListView):
    model = Portfolio_details
    context_object_name = "portfolios"
    template_name = "portfolio-details.html"

