from django.contrib import admin
from portfolio.models import Portfolio , PortfolioCategory
from django.utils.html import format_html

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ( 'img','title','description','user', 'created_date')
    readonly_fields = ['id']

<<<<<<< HEAD
@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("user", "category", "title")
=======
    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}"style="border-radius: 50%;" />'.format(obj.image.url))
    
admin.site.register( PortfolioCategory)
>>>>>>> e5d73b4daed339bb46d08ce6eb21aea8ca1248e4
