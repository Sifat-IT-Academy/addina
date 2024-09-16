from django.contrib import admin
from portfolio.models import Portfolio , PortfolioCategory
from django.utils.html import format_html

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ( 'img','title','description','user', 'created_date')
    readonly_fields = ['id']

    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}"style="border-radius: 50%;" />'.format(obj.image.url))
    
admin.site.register( PortfolioCategory)