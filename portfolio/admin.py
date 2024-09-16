from django.contrib import admin
from portfolio.models import Portfolio , PortfolioCategory,Portfolio_details
from django.shortcuts import render
from django.utils.html import format_html

# Register your models here.
# Samandar va Norbek

admin.site.register(( PortfolioCategory))

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("img","title","user","created_date","category",'description')
    readonly_fields = ['id']

    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}"style="border-radius: 50%;" />'.format(obj.image.url))
    
@admin.register(Portfolio_details)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("img", "title", "user", "created_date", "category", "slug", 'description')
    readonly_fields = ['id', 'slug'] 

    def img(self, obj):
        if obj.image:
            return format_html('<img width="100" height="100" src="{}" style="border-radius: 50%;" />'.format(obj.image.url))
        return ""

    img.short_description = "Image"
