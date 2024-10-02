from django.shortcuts import render
from django.views.generic import ListView
from .models import Cart,Product
class CartListView(ListView):
    model = Cart
    template_name = 'cart.html'
    context_object_name = 'carts'
    
def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_items'] = self.model.objects.count()  
        context['total_price'] = sum(cart.total_price for cart in self.model.objects.all())  # Umumiy narx
        return context
