from django.contrib import admin
from .models import Product,ProductCategory,ProductComment
from django.utils.html import format_html

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('img','title','description','rating')
    readonly_fields = ['id','rating']
     
    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}"style="border-radius: 50%;" />'.format(obj.image.url))

admin.site.register(ProductCategory)

@admin.register(ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'create_date', 'comment', 'rating')
    readonly_fields = ['id']

     
    