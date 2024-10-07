from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Cart

class CartListView(ListView):
    model = Cart
    template_name = 'cart.html'
    context_object_name = 'carts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_items'] = self.model.objects.count()
        context['total_price'] = sum(cart.product.price * 1 for cart in self.model.objects.all())  # Total price calculation
        return context

# Mahsulotni cartdan o'chirish funksiyasi
def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id)
    cart_item.delete()
    return redirect('cart-page')  # Sahifa nomi urls.py dan olinyapti


# Coupon

# from .models import Coupon

# class CartListView(ListView):
#     model = Cart
#     template_name = 'cart.html'
#     context_object_name = 'carts'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         carts = self.model.objects.filter(user=self.request.user)
#         total_price = sum(cart.product.price * 1 for cart in carts)  # Total price calculation
        
#         coupon_code = self.request.GET.get('coupon_code')  # Get coupon code from GET request
#         coupon_discount = 0
#         coupon_applied = False
        
#         # If a coupon code is provided
#         if coupon_code:
#             try:
#                 coupon = Coupon.objects.get(code=coupon_code)
#                 if coupon.discount_type == 'percentage':
#                     coupon_discount = total_price * (coupon.discount_value / 100)
#                 elif coupon.discount_type == 'fixed':
#                     coupon_discount = coupon.discount_value
#                 coupon_applied = True
#             except Coupon.DoesNotExist:
#                 coupon_discount = 0

#         total_with_discount = total_price - coupon_discount

#         context['total_price'] = total_price
#         context['coupon_discount'] = coupon_discount
#         context['total_with_discount'] = total_with_discount
#         context['coupon_code'] = coupon_code
#         context['coupon_applied'] = coupon_applied
        
#         return context

# # Mahsulotni cartdan o'chirish funksiyasi
# def remove_from_cart(request, cart_id):
#     cart_item = get_object_or_404(Cart, id=cart_id)
#     cart_item.delete()
#     return redirect('cart-page')
