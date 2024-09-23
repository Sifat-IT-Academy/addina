<<<<<<< HEAD
from django.shortcuts import *
from .models import *
from django.core.paginator import Paginator
from django.views.generic import ListView

class PortfolioListView(ListView):
    model = Portfolio
    template_name = 'portfolio.html'
    context_object_name = 'portfolio'
    paginate_by = 3  # Adjust pagination if needed

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = PortfolioCategory.objects.all()
        return context


def portfolio_list_view(request):
    portfolios = Portfolio.objects.all()
    paginator = Paginator(portfolios, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'portfolio/portfolio_list.html', {'page_obj': page_obj})


def portfolio_detail(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, id=portfolio_id)
    return render(request, 'portfolio-details.html', {'portfolio': portfolio})



=======
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
>>>>>>> e5d73b4daed339bb46d08ce6eb21aea8ca1248e4
