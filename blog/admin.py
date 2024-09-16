from django.contrib import admin
from django.shortcuts import render
from .models import Blog,BlogCategory,BlogComment,BlogTag,Blog_details
from django.utils.html import format_html

admin.site.register(BlogTag)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("img","title","user","created_date","category")
    readonly_fields = ['id']

    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}"style="border-radius: 50%;" />'.format(obj.image.url))
    
@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    readonly_fields = ['id']

    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}"style="border-radius: 50%;" />'.format(obj.image.url))
  


@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ("user","comment","created_date","user","created_date","blog")
    readonly_fields = ['id']

    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}"style="border-radius: 50%;" />'.format(obj.image.url))
  

@admin.register(Blog_details)
class Blog_detailsListView(admin.ModelAdmin):
    list_display = ('blog', 'image')
    readonly_fields = ['id']