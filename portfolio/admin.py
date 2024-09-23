from django.contrib import admin
from portfolio.models import Portfolio , PortfolioCategory
from django.utils.html import format_html


@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ( "title","user","img",)
    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}"style="border-radius: 50%;" />'.format(obj.image.url))
    
