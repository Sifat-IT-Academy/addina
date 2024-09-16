from django.contrib import admin
from portfolio.models import Portfolio , PortfolioCategory

# Register your models here.
# Samandar va Norbek

@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("user", "category", "title")