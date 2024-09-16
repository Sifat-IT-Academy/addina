from django.shortcuts import render
from .models  import Portfolio
from django.views.generic import ListView
# def portfolio_view(request):
#     return render(request, "portfolio.html")
class PortfolioListView(ListView):
    model = Portfolio
    context_object_name = "portfolio"
    template_name = "portfolio.html"
    
def portfolio_details_view(request):
    return render(request, "portfolio-details.html")
