from django.shortcuts import render

def portfolio_view(request):
    return render(request, "portfolio.html")

def portfolio_details_view(request):
    return render(request, "portfolio-details.html")
