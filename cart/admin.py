from django.contrib import admin
from .models import Cart

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product') 
    list_filter = ('is_active',)
#Amal